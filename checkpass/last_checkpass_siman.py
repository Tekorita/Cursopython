import os
import pandas as pd

# from datetime import (
#     date,
#     datetime,
# )

from scrapers.apps.base.base_scraper import BaseScraper
from scrapers.apps.base.utils.file_services import FileServices
from scrapers.apps.base.domain.type_report import TypeReport
from scrapers.apps.base.exceptions.scraper_exception import ScraperException


class SimanFarmaciaScraper(BaseScraper):

    # def __init__(self, portal, user_data, downloads=None, **kwargs):
    #     super().__init__(portal, user_data, downloads, **kwargs)
    #     self.last_update_need_login = False
    #     self.today = date.today()

    def preprocess_file(self, file_path, report_type, **kwargs):
        file_path_out = f'{os.path.splitext(file_path)[0]}.csv'
        # get csv from xls file
        FileServices.xls_to_csv_transform_file(
            file_path_in=file_path,
            file_path_out=file_path_out,
            headers=True,
        )
        FileServices.delete_first_line(file_path=file_path_out)
        FileServices.remove_file(file_path=file_path)
        return super().preprocess_file(file_path_out, report_type, **kwargs)

    def post_validation_process_file(self, file_path, report_type, **kwargs):
        date_file = kwargs.get('begin_date') or kwargs.get('date_file')

        if report_type == TypeReport.SALES and date_file is None:
            raise ScraperException('error-file-need-begin-date')

        df = pd.read_csv(file_path, dtype=str)
        if TypeReport.SALES:
            df['Fecha'] = str(date_file)

        df.to_csv(file_path, index=False)

    def _do_login(self, username, password, **kwargs):
        payload = self.base_services.get_dict_with_updated_values(
            dictionary = {
                'Usuario': username,
                'Clave': password,
            },
        )
        status_result = self.portal_auth_services.do_login(
            data_login=payload,
            headers=self.portal.headers,
            check_auth_func=self.check_auth_func,
            encode_payload=False,
        )
        return status_result

    def check_auth_func(self, response):
        error_status_code = None
        if 'Usuario o contraseña equivocada.' in response.text:
            error_status_code = 'error-wrong-credentials'

        return error_status_code
