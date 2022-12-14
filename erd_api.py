import re
import json
from sys import argv
from pysnmp.hlapi import *
from pysnmp.entity.rfc3413.oneliner import cmdgen


class Device:

    def __init__(self, ip, ro, oids, port=161):
        self.ip = ip
        self.ro = ro
        self.oids = oids
        self.port = port
        self.if_oids = ['ifAdminStatus', 'ifOperStatus', 'ifInOctets', 'ifOutOctets']

    def get_ifwalk(self):
        pass


if __name__ == "__main__":
    name_script, ip, ro, oid = argv
    device = Device('192.168.1.2', ro, oid)

    print(json.dumps(device.get_ifwalk()))
