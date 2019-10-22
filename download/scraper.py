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

#descarga siman farmacia

import logging
import os
import pandas as pd

from scrapers.apps.base.base_scraper import BaseScraper
from scrapers.apps.base.utils.file_services import FileServices
from scrapers.apps.base.domain import (
    TypeReport,
    DownloadStatusResult,
)
from scrapers.apps.base.exceptions.scraper_exception import ScraperException
from scrapers.apps.base.utils.request_services import RequestServices
from scrapers.apps.base.utils.parsers import (
    split_by_regex,
    unescape_html_strings,
)
from scrapers.apps.locatel.services import (
    find_headers_by_html,
    save_in_store,
    split_local_description,
)
from .properties import props

logger = logging.getLogger(__name__)

    def __init__(self, portal, user_data, downloads=None, **kwargs):
        super().__init__(portal, user_data, downloads, **kwargs)
        self.request_services = RequestServices(self.session, self.portal.headers)
        #self.last_update_need_login = False

    def _download_sales(self, download):
        results = []
        category_id = download['category_id']
        #import pdb; pdb.set_trace()
        for daily_date in download['dates']:
            logger.info(f"sales download file for date: {daily_date}")
            file_name = self.base_services.get_file_name(
                category_id=category_id,
                client_id=self.client_id,
                portal_name=self.portal.name,
                report_type=TypeReport.SALES,
                start_date=daily_date,
                end_date=daily_date,
                ext='html',
            )

            payload = self.base_services.get_dict_with_updated_values(
                dictionary=props['sales_download_data'],
                # Fecha1=daily_date,
                # Fecha2=daily_date,
            )

            # import pdb; pdb.set_trace()
            request_result = self.request_services.post(
                url=props['download_url'],
                headers=props['download_headers'],
                data=payload,
            )
            #import pdb; pdb.set_trace()
            if request_result.status:
                response = request_result.get_property('response')
                result = self.download_sales_file(
                    begin_date=daily_date,
                    end_date=daily_date,
                    file_name=file_name,
                    response=response,
                    category_id=category_id,
                    date_file=daily_date,
                )

            else:
                error_status_code = request_result.get_error_status_code()
                result = DownloadStatusResult.explode(
                    status=False,
                    error_status_code=error_status_code,
                    category_id=category_id,
                    drange=daily_date,
                )
            #import pdb; pdb.set_trace()
            results.extend(result)

        return results

# curl -X POST \
#  http://localhost:8001/api/v1/scraper/farmacia-siman/download/ \
#  -H 'Content-Type: application/json' \
#  -d '{
#    "user_data": {
#        "username": "genomma",
#        "password": "Goicochea01",
#        "country": "HN"
#    },
#    "downloads": [
#        {
#            "category_id": 0,
#            "type": "ventas",
#            "dates": [
#                "2019-09-08",
#                "2019-09-08"
#            ]
#        }
#    ]
# }'


#Properties

BASE_URL = 'https://www.farmaciasiman.me'
props = {    
    'headers_html': [
        'Sucursal',
        'Ciudad',
        'Código',
        'Descripción',
        'Cantidad',
        'Venta',
    ],
    'download_headers': {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'es-419,es;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'www.farmaciasiman.me',
        'Origin': 'https://www.farmaciasiman.me',
        'Referer': 'https://www.farmaciasiman.me/farmacia/lab/vtas_lab_rango_fechas.php',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': (
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 ' 
            '(KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
        ),
        'X-Requested-With': 'XMLHttpRequest',
    },
    'download_url': 'https://www.farmaciasiman.me/farmacia/lab/vtas_lab_rango_fechas2.php',
    'sales_download_data': {
        'Fecha1': '08/09/2019',
        'Fecha2': '08/09/2019',
        'VentaTipo': '5',
        'Ciudad': 'TODAS',
        'Sucursal': 'TODAS',
        'Prov_ID': '0159',
        'Producto': '1',
    },
}

# curl -X POST \
#  http://localhost:8001/api/v1/scraper/farmacia-siman/download/ \
#  -H 'Content-Type: application/json' \
#  -d '{
#    "user_data": {
#        "username": "genomma",
#        "password": "Goicochea01",
#        "country": "HN"
#    },
#    "downloads": [
#        {
#            "category_id": 0,
#            "type": "ventas",
#            "dates": [
#                "2019-09-08",
#                "2019-09-08"
#            ]
#        }
#    ]
# }'


curl -X POST \
  http://stage.b2b.scrapers.instoreview.cl:82/api/v1/scraper/farmacia-siman/download/ \
  -H 'Content-Type: application/json' \
  -d '{
    "user_data": {
        "username": "genomma",
        "password": "Goicochea01",
        "country": "HN",
        "rut": null,
        "client_id": 0
    },
    "downloads": [
        {
            "category_id": 0,
            "type": "ventas",
            "dates": [
                "2019-09-07",
                "2019-09-08"
            ]
        }
    ]
}'