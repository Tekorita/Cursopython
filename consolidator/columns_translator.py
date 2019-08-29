#scrapers/apps/consolidator/transformer/columns_translator.py
# -*- coding: utf-8 -*-
from scrapers.apps.consolidator.transformer.columns_translator import ColumnsTranslator
from scrapers.apps.base.models import Store


class ProConsumoColumnsTranslator(ColumnsTranslator):

    def parse_date(self, value, **kwargs):
        kwargs.update({'dayfirst': True})
        return super(ProConsumoColumnsTranslator, self).parse_date(value, **kwargs)

    def parse_cod_local(self, value):
        code_value = Store.objects.get_code(self.portal, value)
        return super(ProConsumoColumnsTranslator, self).parse_cod_local(code_value)
