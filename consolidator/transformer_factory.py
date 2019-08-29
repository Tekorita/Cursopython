#scrapers/apps/consolidator/transformer/transformer_factory.py
# -*- coding: utf-8 -*-
from scrapers.apps.salcobrand_new.consolidator.transformer import NewSalcobrandTransformer
from scrapers.apps.bbr.consolidator.transformer import BBRTransformer
from scrapers.apps.bbr.consolidator.cencosudcl_transformer import CencosudCLTransformer
from scrapers.apps.cenbiz.consolidator.transformer import CenbizTransformer
from scrapers.apps.maicao.consolidator.transformer import MaicaoTransformer
from scrapers.apps.soriana.consolidator.transformer import SorianaTransformer
from scrapers.apps.walmart.consolidator.transformer import WalmartCLTransformer
from scrapers.apps.prove_comer.consolidator.transformer import ProveComerTransformer
from scrapers.apps.liverpool.consolidator.transformer import LiverpoolTransformer
from scrapers.apps.ripley.consolidator.transformer import RipleyTransformer
from scrapers.apps.oxxo.consolidator.transformer import OxxoTransformer
from scrapers.apps.anonima.consolidator.transformer import AnonimaTransformer
from scrapers.apps.casaley.consolidator.transformer import CasaleyTransformer
from scrapers.apps.alianza.consolidator.transformer import AlianzaTransformer
from scrapers.apps.pcfactory.consolidator.transformer import PcFactoryTransformer
from scrapers.apps.cornershop.consolidator.transformer import CornershopTransformer
from scrapers.apps.dimerc.consolidator.transformer import DimercTransformer
from scrapers.apps.walmart.consolidator.sams_transformer import SamsTransformer
from scrapers.apps.costco.consolidator.transformer import CostcoTransformer
from scrapers.apps.canontex.consolidator.transformer import CanontexTransformer
from scrapers.apps.heb.consolidator.transformer import HebTransformer
from scrapers.apps.rabie.consolidator.transformer import RabieTransformer
from scrapers.apps.keylogistics.consolidator.transformer import KeyLogisticsTransformer
from scrapers.apps.almendariz.consolidator.transformer import AlmendarizTransformer
from scrapers.apps.quimica_suiza.consolidator.transformer import QuimicaSuizaTransformer
from scrapers.apps.pasteur.consolidator.transformer import PasteurTransformer
from scrapers.apps.makro.consolidator.transformer import NewMakroTransformer
from scrapers.apps.home_depot.consolidator.transformer import HomeDepotTransformer
from scrapers.apps.cmr.consolidator.transformer import CMRTransformer
from scrapers.apps.fda.consolidator.transformer import FDATransformer
from scrapers.apps.sanborns.consolidator.transformer import SanbornsTransformer
from scrapers.apps.monroe.consolidator.transformer import MonroeTransformer
from scrapers.apps.salesforce.consolidator.transformer import SalesForceTransformer
from scrapers.apps.proconsumo.consolidator.transformer import ProConsumoTransformer
from scrapers.apps.farmacity.consolidator.transformer import FarmaCityTransformer
from scrapers.apps.consolidator.transformer import Transformer


class TransformerFactory:

    @staticmethod
    def get_transformer(portal, client_id, *args, **kwargs):
        if portal.transformer_class:
            return eval(portal.transformer_class)(portal, client_id, *args, **kwargs)

        raise NotImplementedError(f'Transformer class for {portal} not found')
