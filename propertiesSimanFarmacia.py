props = {
    'download_headers': {
        'sales': {
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
        'stock': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'es-419,es;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'www.farmaciasiman.me',
            'Origin': 'https://www.farmaciasiman.me',
            'Referer': 'https://www.farmaciasiman.me/farmacia/lab/inventarios.php',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': (
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
            ),
            'X-Requested-With': 'XMLHttpRequest',            
        }
    },
    'download_url': {
        'sales': 'https://www.farmaciasiman.me/farmacia/lab/vtas_lab_rango_fechas2.php',
        'stock': 'https://www.farmaciasiman.me/farmacia/lab/inventarios2.php',
    },
    'download_data': {
        'sales': {
            'VentaTipo': '5',
            'Ciudad': 'TODAS',
            'Sucursal': 'TODAS',
            'Prov_ID': '0159',
            'Producto': '1',
        },
        'stock': {
            'Prov_ID': '0159',
            'Sucursal': 'TODAS',
            'Ciudad': 'TODAS',
            'tipo': '1',
            'Productos': '1',
        },
    },
}
