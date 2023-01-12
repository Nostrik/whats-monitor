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

    def is_miner(self):
        return 'WM'

    def get_info(self):
        miner_info = f"Miner type: {self.name}, ip: {self.ip_address}\n"\
                     f"Errors: {self.error_code}, Up Time: {self.up_time}\n"\
                     f"Power: {self.power_w}, Hash-rate: {self.ths_rt}\n"\
                     f"Speed In: {self.speed_in}, Speed out: {self.speed_out}\n"\
                     f"Temperature: {self.temperature}"
        return miner_info


@dataclass
class Innosilicon:

    name: str
    ip_address: str
    user: str
    miner_type: str
    up_time: str
    accepted_rate: list
    fan_duty: str
    total_hash: str
    other_info: dict

    def is_miner(self):
        return

    def get_info(self):
        miner_info = f"Miner type: {self.name}, ip: {self.ip_address}\n"\
                     f"User: {self.user}, Fan duty: {self.fan_duty}\n"\
                     f"Hash-rate: {self.total_hash}"
        return miner_info


@dataclass
class NotAvailableMiner:

    ipaddress: str
    error_msg: str

    def is_miner(self):
        return 'NoneType'
