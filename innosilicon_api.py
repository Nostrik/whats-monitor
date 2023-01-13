from dragon_rest.dragons import DragonAPI
from pprint import pprint
from typing import Type
import logging

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(
    level=logging.INFO,
    # filename='whats-log.txt',
    format='%(asctime)s %(name)s.%(funcName)s +%(lineno)s: %(levelname)-8s [%(process)d] %(message)s'
)
logger = logging.getLogger("[innosilicon_api]")

miners = [
    '192.168.1.68',
    '192.168.1.114'
]

dragon_host = miners[1]
api = DragonAPI(
    dragon_host,
    username="admin",
    password="KX26d'"
)


def get_asic_info(host: str, username: str, password: str) -> DragonAPI:
    try:
        response_from_asic = DragonAPI(host, username=username, password=password)
        # logger.debug(type(response_from_asic))
        return response_from_asic
    except Exception as error:
        logger.exception(error)


def get_summary(response: DragonAPI) -> dict:
    try:
        summary_from_asic = response.summary()
        # logger.debug(type(summary_from_asic))
        return summary_from_asic
    except Exception as er:
        logger.exception(er)
