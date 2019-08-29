#scrapers/apps/proconsumo/consolidator/transformer.py
# -*- coding: utf-8 -*-
from scrapers.apps.consolidator.transformer import Transformer
from .columns_translator import ProConsumoColumnsTranslator


class ProConsumoTransformer(Transformer):

    def get_sales_translator_class(self):
        return ProConsumoColumnsTranslator

    def get_stock_translator_class(self):
        return ProConsumoColumnsTranslator
