from whatsminer import WhatsminerAccessToken, WhatsminerAPI
from pprint import pprint
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("[miners_api]")

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

token = WhatsminerAccessToken(ip_address="192.168.1.40")
summary_json = WhatsminerAPI.get_read_only_info(access_token=token, cmd="summary")

# for asic_info in w_miners:
#     tokens.append(WhatsminerAccessToken(ip_address=asic_info[0], admin_password=asic_info[1]))
#
# for token in tokens:
#     asic_responses.append(WhatsminerAPI.get_read_only_info(access_token=token, cmd="summary"))


def get_access_token(ip_addr: str):
    try:
        token_for_access = WhatsminerAccessToken(ip_address=ip_addr)
        logger.debug(token_for_access)
        return token_for_access
    except Exception as er:
        logger.exception(er)


def get_asic_info_with_token(token):
    try:
        info = WhatsminerAPI.get_read_only_info(access_token=token, cmd="summary")
        return info
    except Exception as er:
        logger.exception(er)


if __name__ == "__main__":

    for a in w_miners:
        tokens.append(get_access_token(a))
    # asic_responses.append(get_asic_info_with_token(tokens[0]))
    # asic_responses.append(get_asic_info_with_token(tokens[1]))
    # asic_responses.append(get_asic_info_with_token(tokens[2]))
    asic_responses.append(get_asic_info_with_token(tokens[3]))
    asic_responses.append(get_asic_info_with_token(tokens[4]))
    asic_responses.append(get_asic_info_with_token(tokens[5]))
    pprint(asic_responses, depth=3)
    print(len(asic_responses))
