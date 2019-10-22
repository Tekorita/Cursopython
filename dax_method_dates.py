    @staticmethod
    def get_validate_labels(response):
        # import pdb; pdb.set_trace()
        # with open('scrapers/apps/dax/tests/inputs/files_test_download.html', 'r') as file:
        #     sopita = BeautifulSoup(file.read(), 'html.parser')
        #     soup_string = str(sopita)
        # import pdb; pdb.set_trace()
        soup = BeautifulSoup(response, 'html')
        section = soup.find('section', class_='section-pdd-sm')
        labels = []

        for files in section.find_all('button'):
            extract_values = {}
            values = files.text
            period = values[6:9]
            # date_transform = f'{values[16:20]}-{values[20:22]}'
            year = int(values[16:20])
            week = int(values[20:22])
            # if extract_values['period'] == 'Men':
            #     pass
                # last_day = get_last_day_of_the_month(year=year, month=week)
                # date_format = r'%Y-%m-%d'
                # first_day_month = datetime.strptime(
                #     f'{date_transform}-01',
                #     date_format,
                # ).date()
                # last_day_month = datetime.strptime(
                #     f'{date_transform}-{last_day}',
                #     date_format,
                # ).date()
                # extract_values['begin_date'] = first_day_month
                # extract_values['end_date'] = last_day_month
            if period == 'Sem':
                extract_values['file'] = f'{props["download_file"]}/{files.text}'
                extract_values['period'] = period
                last_day_week = get_date_by_week_number(
                    year=year,
                    week=week,
                    start_day=0
                )
                first_day_week = find_near_date(
                    pivot_date=last_day_week,
                    search_day=0
                )
                extract_values['begin_date'] = first_day_week
                extract_values['end_date'] = last_day_week
            labels.append(extract_values)
        import pdb; pdb.set_trace()    
        return labels


curl -X POST \
    http://localhost:8001/api/v1/scraper/farmacias-peruanas/download/ \
    -H 'Content-Type: application/json' \
    -d '{
        "user_data": {
            "client_id": "207", 
            "username": "47709240",
            "password": "Farmacia2019",
            "country": "PE",
            "rut": null
        }, 
        "downloads": [
            {
                "category_id": 4773,
                "type": "ventas",
                "dates": ["2019-10-13"],
                "extra_config": {
                    "proveedor": {
                        "pvkey": 290,
                        "name": "JOHNSON & JOHNSON DEL PERU S.A [SURT. GEN\u00c9RICO]",
                        "code": "10000543",
                        "index": 0,
                        "marks": [
                            {
                                "id": 1,
                                "code": "SIN MARCA",
                                "index": 0
                            }
                        ],
                        "category_name": "JOHNSON & JOHNSON DEL PERU S.A [SURT. GEN\u00c9RICO]"
                    },
                    "config_values": {
                        "only_active_products": {
                            "key_translate": "P. activos",
                            "domain": [true, false],
                            "default": false,
                            "chosen": false
                        },
                    "exclude_without_inventory_and_sales": {
                        "key_translate": "Excluir P. sin ventas ni stock",
                        "domain": [true, false],
                        "default": false,
                        "chosen": false},
                        "is_premium": {
                            "key_translate": "Es premium",
                            "domain": [false, false],
                            "default": false,
                            "chosen": false
                        }
                    }
                }
            },
            {
                "category_id": 4774,
                "type": "stock",
                "dates": ["2019-10-13"],
                "extra_config": {
                    "proveedor": {
                        "pvkey": 290,
                        "name": "JOHNSON & JOHNSON DEL PERU S.A [SURT. GEN\u00c9RICO]",
                        "code": "10000543",
                        "index": 0,
                        "marks": [{"id": 1, "code": "SIN MARCA", "index": 0}],
                        "category_name": "JOHNSON & JOHNSON DEL PERU S.A [SURT. GEN\u00c9RICO]"
                    },
                    "config_values": {
                        "only_active_products": {
                            "key_translate": "P. activos",
                            "domain": [true, false],
                            "default": false,
                            "chosen": false
                        },
                        "exclude_without_inventory_and_sales": {
                            "key_translate": "Excluir P. sin ventas ni stock",
                            "domain": [true, false],
                            "default": false,
                            "chosen": false
                        },
                        "is_premium": {
                            "key_translate": "Es premium",
                            "domain": [true, false],
                            "default": true,
                            "chosen": true
                        }
                    }
                }
            }
        ]
    }'