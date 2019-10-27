import logging
import os
import pandas as pd

from scrapers.apps.base.base_scraper import BaseScraper
from scrapers.apps.base.utils.file_services import FileServices
from scrapers.apps.base.domain import TypeReport
from scrapers.apps.base.exceptions.scraper_exception import ScraperException
from scrapers.apps.base.utils.request_services import RequestServices
from .properties import props


logger = logging.getLogger(__name__)


class SimanFarmaciaScraper(BaseScraper):

    def __init__(self, portal, user_data, downloads=None, **kwargs):
        super().__init__(portal, user_data, downloads, **kwargs)
        self.request_services = RequestServices(self.session, self.portal.headers)

    def preprocess_file(self, file_path, report_type, **kwargs):
        file_path_out = f'{os.path.splitext(file_path)[0]}.csv'
        if file_path.endswith('html'):
            file_path = super().preprocess_file(file_path, report_type, **kwargs)
            FileServices.html_table_to_csv(
                file_path_in=file_path,
                file_path_out=file_path_out,
                remove_file=True,
            )
        elif file_path.endswith(('.xls', '.xlsx')):
            FileServices.xls_to_csv_transform_file(
                file_path_in=file_path,
                file_path_out=file_path_out,
                headers=True,
            )
            FileServices.delete_first_line(file_path=file_path_out)
            FileServices.remove_file(file_path=file_path)
            file_path = super().preprocess_file(file_path, report_type, **kwargs)
        else:
            raise ScraperException('error-file-not-supported')

        return file_path_out

    def post_validation_process_file(self, file_path, report_type, **kwargs):
        date_file = kwargs.get('begin_date') or kwargs.get('date_file')
        if date_file is None:
            raise ScraperException('error-file-need-begin-date')

        df = pd.read_csv(file_path, dtype=str)
        df['Fecha'] = str(date_file)
        df.to_csv(file_path, index=False)

    def _do_login(self, username, password, **kwargs):
        payload = {
            'Usuario': username,
            'Clave': password,
        }
        status_result = self.portal_auth_services.do_login(
            data_login=payload,
            headers=self.portal.headers,
            check_auth_func=self.check_auth_func,
            encode_payload=False,
        )
        status_result2 = self.portal_auth_services.do_login(
            data_login=payload,
            headers=self.portal.headers,
            check_auth_func=self.check_auth_func,
            encode_payload=False,
        )
        status_result3 = self.portal_auth_services.do_login(
            data_login=payload,
            headers=self.portal.headers,
            check_auth_func=self.check_auth_func,
            encode_payload=False,
        )
        return status_result

    def check_auth_func(self, response):
        if 'Usuario o contraseña equivocada.' in response.text:
            raise ScraperException('error-wrong-credentials')


    # def __do_download_file(self, category_id, report_type, begin_date, **kwargs):

    def _download_sales_v2(self, downloads, date_range):
        category_id = downloads['category_id']
        file_name = self.base_services.get_file_name(
            category_id=category_id,
            client_id=self.client_id,
            portal_name=self.portal.name,
            report_type=TypeReport.SALES,
            start_date=date_range['start'],
            end_date=date_range['end'],
            ext='html',
        )
        payload = self.base_services.get_dict_with_updated_values(
            dictionary=props['download_data']['sales'],
            Fecha1=date_range['start'].strftime("%d/%m/%Y"),
            Fecha2=date_range['end'].strftime("%d/%m/%Y"),
        )
        request_result = self.request_services.post(
            url=props['download_url']['sales'],
            headers=props['download_headers'],
            data=payload,
        )
        import pdb; pdb.set_trace()
        if request_result.status:
            response = request_result.get_property('response')
            self.download_result_list.extend(
                self.download_sales_file(
                    begin_date=date_range['start'],
                    end_date=date_range['end'],
                    file_name=file_name,
                    response=response,
                    category_id=category_id,
                    date_file=date_range['start'],
                ),
            )
        else:
            ScraperException(request_result.get_error_status_code())
        import pdb; pdb.set_trace()
    # def _download_stock_v2(self, downloads, date_range):
    #     category_id = downloads['category_id']
    #     file_name = self.base_services.get_file_name(
    #         category_id=category_id,
    #         client_id=self.client_id,
    #         portal_name=self.portal.name,
    #         report_type=TypeReport.STOCK,
    #         start_date='',
    #         end_date='',
    #         ext='html',
    #     )
    #     payload = self.base_services.get_dict_with_updated_values(
    #         dictionary=props['download_data']['stock'],
    #         # Fecha1=date_range['start'].strftime("%d/%m/%Y"),
    #         # Fecha2=date_range['end'].strftime("%d/%m/%Y"),
    #     )
    #     request_result = self.request_services.post(
    #         url=props['download_url']['stock'],
    #         headers=props['download_headers'],
    #         data=payload,
    #     )
    #     if request_result.status:
    #         response = request_result.get_property('response')
    #         self.download_result_list.extend(
    #             self.download_sales_file(
    #                 begin_date=date_range['start'],
    #                 # end_date=date_range['end'],
    #                 file_name=file_name,
    #                 response=response,
    #                 category_id=category_id,
    #                 # date_file=date_range['start'],
    #             ),
    #         )
    #     else:
    #         ScraperException(request_result.get_error_status_code())