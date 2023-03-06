from whatsminer import WhatsminerAccessToken, WhatsminerAPI
from pprint import pprint
import logging

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(
    level=logging.INFO,
    # filename='log.txt',
    format='%(asctime)s %(name)s.%(funcName)s +%(lineno)s: %(levelname)-8s [%(process)d] %(message)s'
)
logger = logging.getLogger("[whatsminer_api]")

w_miners = [
    '192.168.1.40',
    '192.168.1.41',
    '192.168.1.53',
    '192.168.1.60',
    '192.168.1.126',
    '192.168.1.151',
]

tokens = []
asic_responses = []


def get_access_token(ip_address: str) -> WhatsminerAccessToken:
    try:
        token_for_access = WhatsminerAccessToken(ip_address=ip_address)
        return token_for_access
    except Exception as er:
        logger.exception(er)


def get_asic_info_with_token(token: WhatsminerAccessToken) -> WhatsminerAPI:
    try:
        info = WhatsminerAPI.get_read_only_info(access_token=token, cmd="summary")
        return info
    except Exception as er:
        logger.exception(er)


# if __name__ == "__main__":
#
#     for a in w_miners:
#         tokens.append(get_access_token(a))
#     for token in tokens:
#         asic_responses.append(get_asic_info_with_token(token))
#     pprint(asic_responses)
#     print(len(asic_responses))
