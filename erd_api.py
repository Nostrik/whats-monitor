import re
import json
from sys import argv
from pysnmp.hlapi import *
from pysnmp.entity.rfc3413.oneliner import cmdgen


def get_value():
    iterator = getCmd(
        SnmpEngine(),
        CommunityData('public', mpModel=0),
        UdpTransportTarget(('192.168.1.2', 161)),
        ContextData(),
        ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))


def send_trap():
    iterator = sendNotification(
        SnmpEngine(),
        CommunityData('public', mpModel=0),
        UdpTransportTarget(('192.168.1.2', 162)),
        ContextData(),
        'trap',
        NotificationType(
            ObjectIdentity('1.3.6.1.6.3.1.1.5.2')
        ).addVarBinds(
            ('1.3.6.1.6.3.1.1.4.3.0', '1.3.6.1.4.1.20408.4.1.1.2'),
            ('1.3.6.1.2.1.1.1.0', OctetString('my system'))
        ).loadMibs(
            'SNMPv2-MIB'
        )
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)


def request_one_iod():
    erd3temperatureSensor0 = '.1.3.6.1.4.1.40418.2.4.4.1.0'
    # errorIndication, errorStatus, errorIndex, varBindTable = cmdgen.nextCmd((
    #     cmdgen.CommunityData(ro_community, mpModel=1),
    #     cmdgen.UdpTransportTarget((net_address, 161)),
    #     ('1.3.6.1.2.1.2.2.1.7'),
    #     ('1.3.6.1.2.1.2.2.1.8'),
    #     ('1.3.6.1.2.1.2.2.1.10'),
    #     ('1.3.6.1.2.1.2.2.1.16')
    # )
    a, b, c, d = cmdgen.nextCmd(

    )


if __name__ == "__main__":
    request_one_iod()
