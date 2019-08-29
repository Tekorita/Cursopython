#scrapers/apps/consolidator/tests/consolidator_tests.py
# -*- coding: utf-8 -*-
import importlib
import inspect
import pytest
import pandas as pd

from copy import deepcopy
from django.apps import apps
from datetime import date

from scrapers.apps.consolidator.consolidator import Consolidator
from scrapers.apps.api.views.scraper.scraper_factory import scraper_factory
from scrapers.apps.base.utils.file_services import FileServices
from .consolidator_input_config import (
    SALES_CONSOLIDATED_COLUMNS,
    STOCK_CONSOLIDATED_COLUMNS,
    get_list_modules_from_folders,
)
from scrapers.apps.base.domain import (
    TypeReport,
    DownloadStatusResult,
)


class TestConsolidator:

    CUMULATIVE_MONTHLY = 'MONTHLY'

    @pytest.mark.parametrize('config_input', get_list_modules_from_folders())
    @pytest.mark.django_db
    def test_consolidate(self, user_data, config_input):
        """
        Test rules:
            * Check the structure of the consolidated output
            * Sum of units, costs and sales of consolidated file must be equal to source file sums
            * Check de rows number (not necessarily equal to the input)
        """
        config_input = self.import_modules(config_input)
        Portal = apps.get_model('base', 'Portal')
        portal = Portal.objects.get(
            name=config_input['portal'],
            iso2_code=config_input['iso2_code'],
        )
        user_data.update({
            'iso2_code': config_input['iso2_code'],
            'country': config_input['iso2_code'],
        })

        scraper = self.import_modules(self.get_app_module(portal.scraper_class))(portal, user_data)

        for file_input in config_input['file_inputs']:
            params, extra_params = self.validate_test_input_params(deepcopy(file_input))
            source_path, ext = params['source'].split('.')
            copy_of_source_path = source_path + '-copy.' + ext
            FileServices.copy_file(
                path_file_in=params['source'],
                path_file_out=copy_of_source_path,
            )
            results = Consolidator(
                scraper=scraper,
                client_id=0,
            ).consolidate(
                category_id=0,
                report_type=params['type'],
                file_path=copy_of_source_path,
                **extra_params
            )

            FileServices.remove_file('{}.csv'.format(copy_of_source_path.split('.')[0]))

            units_sum = 0
            cost_value_sum = 0
            sales_value_sum = 0
            rows = 0

            expected_dates_result = params['expected_dates_result']
            if bool(expected_dates_result):
                assert len(expected_dates_result) == len(results)

            for idx, result in enumerate(results):
                self.assert_result(
                    status_result=result,
                    report_type=file_input['type'],
                    expected_error=params['expected_error'],
                    expected_properties=params['expected_properties'],
                    portal=portal,
                )

                if result.status and result.s3_key:
                    df = pd.read_csv(result.s3_key, delimiter=';')
                    self.check_consolidated_structure(df=df, report_type=file_input['type'])
                    self.match_consolidation_result(
                        df=df,
                        result=result,
                        expected_dates_result=expected_dates_result,
                        date_index=idx,
                    )
                    units_sum += df['Unidades'].sum()
                    cost_value_sum += df['Valores_Costo'].sum()
                    sales_value_sum += df['Valores_Venta'].sum()
                    rows += df.shape[0]  # count rows without headers

            assert units_sum == params['expected_units_sum']
            assert int(cost_value_sum) == int(params['expected_cost_value_sum'])
            assert int(sales_value_sum) == int(params['expected_sales_value_sum'])
            assert rows == params['expected_content_rows']

    @staticmethod
    def assert_result(status_result, **kwargs):
        """
        Validate result data.
        :param status_result: DownloadStatusResult object
        :param kwargs:
        :return:
        """
        assert isinstance(status_result, DownloadStatusResult)

        if status_result.get_status():
            assert (
                status_result.s3_key is not None
                or status_result.s3_key is None
                and kwargs.get('portal').cumulative == TestConsolidator.CUMULATIVE_MONTHLY
                and status_result.date.split('-')[2] != '01'
            )
        else:
            assert status_result.get_error_status_code() == kwargs['expected_error']

        assert kwargs['report_type'] == status_result.type

        expected_properties = kwargs.get('expected_properties', {})
        if expected_properties:
            assert expected_properties == status_result.properties

    @staticmethod
    def check_consolidated_structure(df, report_type):
        """
        Check structure of consolidation result file.
        :param df: pandas data frame
        :param report_type: string
        :return:
        """
        if report_type == TypeReport.SALES:
            assert df.columns.tolist() == SALES_CONSOLIDATED_COLUMNS
        else:
            assert df.columns.tolist() == STOCK_CONSOLIDATED_COLUMNS

    @staticmethod
    def match_consolidation_result(df, result, **kwargs):
        """
        Check if data consolidation file has match with result data.
        :param df: pandas data frame
        :param result: DownloadStatusResult object
        :return:
        """
        year, month, day = result.date.split('-')

        assert date(int(year), int(month), int(day)) <= date.today()
        assert all(df['Fecha'] == result.date)
        assert all(df['Category_Id'] == result.category_id)

        expected_dates_result = kwargs.get('expected_dates_result', [])
        if bool(expected_dates_result):
            assert expected_dates_result[kwargs['date_index']] == result.date
            assert all(df['Fecha'] == expected_dates_result[kwargs['date_index']])

    @staticmethod
    def import_modules(config_input):
        """
        Import portal consolidation tests module.
        :param config_input: dictionary
        :return: import module
        """
        module, dictionary = config_input
        import_module = importlib.import_module(module)  # noqa
        return eval('import_module.{}'.format(dictionary))

    @staticmethod
    def get_app_module(portal_class):
        """
        Read "scraper_factory.py" file and extract the scraper class module.
        :param portal_class: string
        :return: string
        """
        app_module = ()
        get_file = inspect.getfile(scraper_factory)

        with open(get_file, 'r') as readfile:
            list_modules = [
                module
                for module in readfile.read().split('\n')
                if 'from' in module and 'import' in module and portal_class in module
            ]

            if list_modules:
                module = list_modules[0].replace('from', '').replace('import', '').strip().split()
                app_module = tuple(module)

        return app_module

    @staticmethod
    def validate_test_input_params(input_params):
        """
        Validate input params and decide its ways.
        :param input_params: dictionary
        :return: tuple of dictionaries
        """
        params = {}

        report_type = 'type'
        source_file = 'source'
        expected_units_sum = 'expected_units_sum'
        expected_cost_value_sum = 'expected_cost_value_sum'
        expected_sales_value_sum = 'expected_sales_value_sum'
        expected_content_rows = 'expected_content_rows'

        assert report_type in input_params.keys()
        params[report_type] = input_params.pop(report_type)

        assert source_file in input_params.keys()
        params[source_file] = input_params.pop(source_file)

        assert expected_units_sum in input_params.keys()
        params[expected_units_sum] = input_params.pop(expected_units_sum)

        assert expected_cost_value_sum in input_params.keys()
        params[expected_cost_value_sum] = input_params.pop(expected_cost_value_sum)

        assert expected_sales_value_sum in input_params.keys()
        params[expected_sales_value_sum] = input_params.pop(expected_sales_value_sum)

        assert expected_content_rows in input_params.keys()
        params[expected_content_rows] = input_params.pop(expected_content_rows)

        params['expected_error'] = input_params.pop('expected_error', 'error-empty-file')
        params['expected_properties'] = input_params.pop('expected_properties', {})
        params['expected_dates_result'] = input_params.pop('expected_dates_result', [])

        return params, input_params
