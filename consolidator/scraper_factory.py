#scrapers/apps/api/views/scraper/scraper_factory.py
from scrapers.apps.base.exceptions.scraper_factory_exception import ScraperFactoryException
from scrapers.apps.base.models.portal import Portal
from scrapers.apps.bbr.exceptions import (
    DataRequestIsEmpty,
    PvkeyIsEmpty,
)
from scrapers.apps.almendariz.scraper import AlmendarizScraper
from scrapers.apps.bbr.cencosud_pe_scraper import CencosudPeScraper
from scrapers.apps.bbr.lapolar_scraper import LaPolarScraper
from scrapers.apps.bbr.inka_farma_scraper import InkaFarmaScraper
from scrapers.apps.bbr.ahumada_scraper import AhumadaScraper
from scrapers.apps.bbr.scraper import BBRScraper
from scrapers.apps.bbr.smu_scraper import SmuScraper
from scrapers.apps.bbr.easy_scraper import EasyScraper
from scrapers.apps.bbr.cencosud_ar_scraper import CencosudArScraper
from scrapers.apps.cmr.scraper import CmrScraper
from scrapers.apps.cmr.sodimac_scraper import SodimacScraper
from scrapers.apps.maicao.scraper import MaicaoScraper
from scrapers.apps.preunic.scraper import PreunicScraper
from scrapers.apps.ripley.scraper import RipleyScraper
from scrapers.apps.salcobrand.scraper import SalcobrandScraper
from scrapers.apps.salcobrand_new.scraper import NewSalcobrandScraper
from scrapers.apps.walmart.scraper import WalmartScraper
from scrapers.apps.walmart.new_walmart_scraper import NewWalmartScraper
from scrapers.apps.chedraui.scraper import ChedrauiScraper
from scrapers.apps.cenbiz.scraper import CenbizScraper
from scrapers.apps.makro.scraper import MakroScraper
from scrapers.apps.makro.new_makro_scraper import NewMakroScraper
from scrapers.apps.anonima.scraper import AnonimaScraper
from scrapers.apps.prove_comer.scraper import ProveComerScraper
from scrapers.apps.soriana.scraper import SorianaScraper
from scrapers.apps.oxxo.scraper import OxxoScraper
from scrapers.apps.alianza.scraper import AlianzaScraper
from scrapers.apps.casaley.scraper import CasaleyScraper
from scrapers.apps.cornershop.scraper import CornershopScraper
from scrapers.apps.dimerc.scraper import DimercScraper
from scrapers.apps.pcfactory.scraper import PcFactoryScraper
from scrapers.apps.rabie.scraper import RabieScraper
from scrapers.apps.keylogistics.scraper import KeyLogisticsScraper
from scrapers.apps.canontex.scraper import CanontexScraper
from scrapers.apps.walmart.sams_scraper import SamsScraper
from scrapers.apps.costco.scraper import CostcoScraper
from scrapers.apps.liverpool.scraper import LiverpoolScraper
from scrapers.apps.salcobrand_new.preunic_nuevo_scraper import NewPreunicScraper
from scrapers.apps.heb.scraper import HebScraper
from scrapers.apps.quimica_suiza.scraper import QuimicaSuizaScraper
from scrapers.apps.pasteur.scraper import PasteurScraper
from scrapers.apps.home_depot.scraper import HomeDepotScraper
from scrapers.apps.coppel.scraper import CoppelScraper
from scrapers.apps.fda.scraper import FDAScraper
from scrapers.apps.sanborns.scraper import SanbornsScraper
from scrapers.apps.monroe.scraper import MonroeScraper
from scrapers.apps.salesforce.scraper import SalesForceScraper
from scrapers.apps.farmacity.scraper import FarmaCityScraper
from scrapers.apps.proconsumo.scraper import ProConsumoScraper


__all__ = [
    'AlmendarizScraper',
    'CencosudPeScraper',
    'LaPolarScraper',
    'InkaFarmaScraper',
    'AhumadaScraper',
    'BBRScraper',
    'SmuScraper',
    'EasyScraper',
    'CencosudArScraper',
    'CmrScraper',
    'SodimacScraper',
    'MaicaoScraper',
    'PreunicScraper',
    'RipleyScraper',
    'SalcobrandScraper',
    'NewSalcobrandScraper',
    'WalmartScraper',
    'NewWalmartScraper',
    'ChedrauiScraper',
    'CenbizScraper',
    'MakroScraper',
    'NewMakroScraper',
    'AnonimaScraper',
    'ProveComerScraper',
    'SorianaScraper',
    'OxxoScraper',
    'AlianzaScraper',
    'CasaleyScraper',
    'CornershopScraper',
    'DimercScraper',
    'PcFactoryScraper',
    'RabieScraper',
    'KeyLogisticsScraper',
    'CanontexScraper',
    'SamsScraper',
    'CostcoScraper',
    'LiverpoolScraper',
    'NewPreunicScraper',
    'HebScraper',
    'QuimicaSuizaScraper',
    'HomeDepotScraper',
    'PasteurScraper',
    'CoppelScraper',
    'FDAScraper',
    'SanbornsScraper',
    'MonroeScraper',
    'SalesForceScraper',
    'FarmaCityScraper',
    'ProConsumoScraper',
]


def scraper_factory(portal_name, user_data, downloads=None):
    """ Factory scraper based on scraper_class field of Portal Model """
    portal = get_final_portal(portal_name, user_data['country'])
    if portal.scraper_class:
        try:
            scraper = eval(portal.scraper_class)(
                portal=portal,
                user_data=user_data,
                downloads=downloads,
                portal_name=portal_name,
            )
        except PvkeyIsEmpty:
            raise ScraperFactoryException('error-bbr-pvkey-is-empty')
        except DataRequestIsEmpty:
            raise ScraperFactoryException('error-bbr-data-request-is-empty')
    else:
        raise ScraperFactoryException('error-no-implemented')

    if not scraper.service_is_available():
        raise ScraperFactoryException('error-portal-failed')

    return scraper


def get_final_portal(portal_name, iso2_code):
    portals = Portal.objects.filter(
        iso2_code=iso2_code
    ).extra(
        where=["%s LIKE concat(name, %s)"],
        params=[portal_name, "%"],
    )

    if portals.count() > 1:
        portals = Portal.objects.filter(
            iso2_code=iso2_code,
            name=portal_name,
        )
    if portals.count() == 0:
        raise ScraperFactoryException('error-portal-not-exists')

    return portals[0]


curl -X POST \
  http://localhost:8001/api/v1/scraper/fda/checkpass/ \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache,no-cache,no-cache,no-cache' \
  -d '{
    "username": "P1728",
    "password": "*cx4882mx",
    "country": "MX"
}'
