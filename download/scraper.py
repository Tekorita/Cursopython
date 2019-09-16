# -*- coding: utf-8 -*-
import logging
import pandas as pd
import collections
import base64

from .properties import props
from datetime import (
    date,
    datetime,
)
from scrapers.apps.base.base_scraper import BaseScraper
from scrapers.apps.base.utils.file_services import FileServices
from scrapers.apps.base.utils.request_services import RequestServices

logger = logging.getLogger(__name__)


class FDAScraper(BaseScraper):

    def __init__(self, portal, user_data, downloads=None, **kwargs):
        super(FDAScraper, self).__init__(portal, user_data, downloads, **kwargs)
        self.last_update_need_login = False
        self.today = date.today()

    def preprocess_file(self, file_path, report_type, **kwargs):
        file_path_out = '%s.csv' % file_path.split('.')[0]
        # get csv from xls file
        FileServices.xls_to_csv_transform_file(
            file_path_in=file_path,
            file_path_out=file_path_out,
            headers=True,
        )
        FileServices.remove_file(file_path=file_path)

        return super(FDAScraper, self).preprocess_file(file_path_out, report_type, **kwargs)

    def post_validation_process_file(self, file_path, report_type, **kwargs):
        df = pd.read_csv(file_path, encoding='utf-8')
        headers = df.columns.values.tolist()[:11]
        dates_dict = collections.OrderedDict()
        df.rename(columns={'MES ACTUAL': 'MES -0'}, inplace=True)
        date_column_value = df.iloc[:, -1][0]
        newest_date = datetime.strptime(date_column_value, '%Y/%m/%d').replace(day=1)
        for i in range(0, 4):
            dates_dict['MES -{}'.format(i)] = newest_date.replace(month=newest_date.month - i).strftime('%d-%m-%Y')  # noqa

        df.rename(
            columns=dates_dict,
            inplace=True,
        )
        df2 = pd.melt(
            frame=df,
            id_vars=headers,
            value_vars=list(dates_dict.values()),
            var_name='FECHA',
            value_name='UNIDADES',
        )

        df2.to_csv(file_path, index=False, encoding='utf-8')

        return file_path

    def _do_login(self, username, password, **kwargs):
        pass_encrypt = base64.b64encode(bytes(password, 'utf-8')).decode()
        payload = self.base_services.get_dict_with_updated_values(
            dictionary = props['login_data'],
            usr_id=username,
            usr_pswd=pass_encrypt,
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
        if 'INVALID' in response.url:
            error_status_code = 'error-wrong-credentials'

        return error_status_code

    # def _download_stock(self, download):
    #     download_date = download['dates'][0]

    #     return DownloadStatusResult(
    #         status=False,
    #         error_status_code='error-stock-type-not-implemented',
    #         category_id=download['category_id'],
    #         report_type=TypeReport.STOCK,
    #         date=download_date,
    #     )

#cuando me logueo
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Content-Length: 234
Content-Type: text/html; charset=UTF-8
Date: Fri, 23 Aug 2019 20:20:17 GMT
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Location: https://spt.fahorro.com.mx/fahcolprd/index.php?mode=rp|default&mcs_form=rp%7Clogin_prompt&modal_status=
Pragma: no-cache
Server: Microsoft-IIS/7.5
Set-Cookie: 259b0c2ad1218404ad131c278608f217=%3AnJ.%25%7ELgmy%3AsYy%5BXJy+%28L6gc4ab%5BG%5E%29H; expires=Fri, 23-Aug-2019 20:40:17 GMT
Set-Cookie: usr_id=u%2CNyy; expires=Fri, 06-Sep-2019 20:20:17 GMT
X-Powered-By: PHP/5.2.9
X-Powered-By: ASP.NET
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Content-Length: 185
Content-Type: application/x-www-form-urlencoded
Cookie: usr_id=u%2CNyy; 259b0c2ad1218404ad131c278608f217=%3AnJ.%25%7ELgmy%3AsYy%5BXJy+%28L6gc4ab%5BG%5E%29H
Host: spt.fahorro.com.mx
Origin: https://spt.fahorro.com.mx
Referer: https://spt.fahorro.com.mx/fahcolprd/index.php?mode=rp|login_prompt
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36

https://spt.fahorro.com.mx/fahcolprd/index.php?estado_desc=YUCATAN&mundo=&producto_code=&division=&dda_id=LST-VAR-STK-SUC&mode=rp%7Cdisplay_results&mcs_form=LST-VAR-STK-SUC&modal_status=&form_fields=estado_desc%2Cproducto_code%2Cmundo%2Cdivision%2Cdda_id%2Cmode

    YUCATAN
	QUERETARO
	PUEBLA
	DURANGO
	MORELOS
	TABASCO
	COAHUILA
	SAN LUIS POTOSI
	ESTADO DE MEXICO
	CIUDAD DE MEXICO


    def preprocess_file(self, file_path, report_type, **kwargs):
        file_path_out = f'{os.path.splitext(file_path)[0]}.csv'
        
        if report_type == TypeReport.STOCK:
            csv_files = []
            decompress_folder = f'fda-stock-files-{self.client_id}-{self.portal.iso2_code}'
            FileServices.create_directory(decompress_folder)           
            self.zip_services.unzip_all(
                file_name_zip=file_path,
                destination=decompress_folder,
            )

            file_list = [
                os.path.join(str(decompress_folder)+'/stock', r_file)
                for r_file in os.listdir(str(decompress_folder)+'/stock')
                if r_file.endswith(props['expected_ext_files'])
            ]
            
            for idx, extracted_file in enumerate(file_list):
                data_xls = pd.read_excel(extracted_file, index_col=None)
                data_xls.to_csv(str(decompress_folder)+ f'/stock/{idx}.csv', encoding='utf-8', index=False,)  # NOQA
                csv_file = str(decompress_folder)+f'/stock/{idx}.csv'
                csv_files.append(csv_file)

            file_path_out = FileServices.merge_csv(
                file_paths=csv_files,
                final_path=file_path_out,
                remove_source_files=True,
            )

            FileServices.remove_folder(decompress_folder)
            
        return file_path_out