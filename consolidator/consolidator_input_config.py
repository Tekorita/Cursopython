#scrapers/apps/consolidator/tests/consolidator_input_config.py

# -*- coding: utf-8 -*-
import os


DATA_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'consolidator_input')

CONFIG_INPUT = {
    'module': 'scrapers.apps.consolidator.tests.consolidator_input.{portal_folder}.config',
    'dictionary': 'config_input',
}

SALES_CONSOLIDATED_COLUMNS = [
    'Cliente',
    'Category_Id',
    'Fecha',
    'Cadena',
    'Cod_Prod_Cadena',
    'Descripcion_Prod_Cadena',
    'Cod_Local',
    'Descripcion_Local',
    'Unidades',
    'Valores_Costo',
    'Valores_Venta',
]
STOCK_CONSOLIDATED_COLUMNS = SALES_CONSOLIDATED_COLUMNS + [
    'Sugerido',
    'Mix',
    'Transito',
]


def get_list_modules_from_folders():
    list_folder = [
        folder
        for folder in os.listdir(DATA_FOLDER)
        if os.path.isdir(os.path.join(DATA_FOLDER, folder)) and os.path.exists(os.path.join(DATA_FOLDER, folder, 'config.py'))  # NOQA
    ]

    list_modules = [
        (CONFIG_INPUT['module'].format(portal_folder=folder), CONFIG_INPUT['dictionary'])
        for folder in list_folder
    ]
    list_modules = [
        (
            'scrapers.apps.consolidator.tests.consolidator_input.proconsumo_HN.config',
            'config_input',
        )
    ]

    return list_modules
