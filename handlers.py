import logging
from models import Whatsminer, Innosilicon
from whatsminer_api import get_access_token, get_asic_info_with_token
from innosilicon_api import get_asic_info, get_summary
from config import glob_miners_list

logging.basicConfig(level=logging.DEBUG)
handler_logger = logging.getLogger('[handlers]')


def get_one_whatsminer_with_api(miner_ip_address: str):
    miner_token = get_access_token(ip_address=miner_ip_address)
    miner_summary = get_asic_info_with_token(token=miner_token)
    try:
        miner_object = Whatsminer(
            name='Whatsminer',
            ip_address=miner_ip_address,
            miner_type='[miner_type]',
            error_code=miner_summary['SUMMARY'][0]['Error Code Count'],
            up_time=miner_summary['SUMMARY'][0]['Uptime'],
            ths_rt=miner_summary['SUMMARY'][0]['HS RT'],
            ths_avg='[ths_avg]',
            power_w=miner_summary['SUMMARY'][0]['Power'],
            freq_avg='[freq_avg]',
            speed_in=miner_summary['SUMMARY'][0]['Fan Speed In'],
            speed_out=miner_summary['SUMMARY'][0]['Fan Speed Out'],
            temperature=miner_summary['SUMMARY'][0]['Temperature'],
            worker='[worker]',
            other_info={'other_info': 'none'}
        )
        handler_logger.info(f'miner - ip: {miner_ip_address} type: whatsminer, was answered')
        return miner_object
    except Exception as er:
        handler_logger.exception(er)


def get_one_innosilicon_with_api(miner_ip_address: str, username='admin', password="KX26d'"):
    asic_info = get_asic_info(host=miner_ip_address, username=username, password=password)
    asic_summary = get_summary(asic_info)
    try:
        miner_object = Innosilicon(
            name='Innosilicon',
            ip_address=miner_ip_address,
            user=asic_summary['POOLS'][0]['User'],
            miner_type='[miner_type]',
            up_time='[up_time]',
            accepted_rate=[
                asic_summary['POOLS'][0]['Accepted'],
                asic_summary['POOLS'][1]['Accepted'],
                asic_summary['POOLS'][2]['Accepted'],
            ],
            fan_duty=asic_summary['HARDWARE'],
            total_hash=asic_summary['TotalHash'],
            other_info={'other_info': 'none'}
        )
        handler_logger.info(f'miner - ip: {miner_ip_address} type: innosilicon, was answered')
        return miner_object
    except Exception as er:
        handler_logger.exception(er)


def get_all_miners():
    miners_obj_list = []
    for miner_note in glob_miners_list:
        if miner_note['code_name'] == 'WM':
            miners_obj_list.append(get_one_whatsminer_with_api(miner_note['ip']))
        elif miner_note['code_name'] == 'IS':
            miners_obj_list.append(get_one_innosilicon_with_api(miner_note['ip']))
        else:
            handler_logger.error('There is no handler for this equipment')
    return miners_obj_list
