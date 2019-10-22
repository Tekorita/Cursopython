#scrapers/apps/consolidator/tests/consolidator_input/proconsumo_HN/config.py
# -*- coding: utf-8 -*-
import os

from scrapers.apps.base.domain import TypeReport


DATA_FOLDER = os.path.dirname(os.path.abspath(__file__))


config_input = {
    'portal': 'proconsumo',
    'iso2_code': 'HN',
    'file_inputs': [
        {
            'type': TypeReport.SALES,
            'source': os.path.join(DATA_FOLDER, 'ventas.csv'),
            'expected_units_sum': -8597,
            'expected_cost_value_sum': -750.69,
            'expected_sales_value_sum': -750.69,
            'expected_content_rows': 12,
        },
    ],
}
