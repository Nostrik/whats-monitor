from dataclasses import dataclass


@dataclass
class Whatsminer:

    name: str
    ip_address: str
    miner_type: str
    error_code: str
    up_time: str
    ths_rt: str
    ths_avg: str
    power_w: str
    freq_avg: str
    speed_in: str
    speed_out: str
    temperature: str
    worker: str
    other_info: dict


@dataclass
class Innosilicon:

    name: str
    ip_address: str
    user: str
    miner_type: str
    up_time: str
    accepted_rate: str
    fan_duty: str
    total_hash: str
    other_info: dict
