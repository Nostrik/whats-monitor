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

    target_value = '.1.3.6.1.4.1.40418.2.4.4.1.0'  # Name/OID: erd3temperatureSensor.0; Value (Integer): 26
    target_value2 = '.1.3.6.1.4.1.40418.2.4.4.2.2.0'  # Name/OID: erd3temperatureSensorOut1.0; Value (Integer): 21
    target_value3 = '.1.3.6.1.4.1.40418.2.4.2.3.0'  # Name/OID: erd3remoteControlContact11.0; Value (Integer): manON(0)
    target_value4 = '.1.3.6.1.4.1.40418.2.4.2.1.0'  # Name/OID: erd3resetSmartContact10.0; Value (Integer): bypass(0)

    g = getCmd(SnmpEngine(),
                CommunityData('public', mpModel=0),
                UdpTransportTarget(('192.168.1.2', 161)),
                ContextData(),
                ObjectType(ObjectIdentity(target_value2)))

    errorIndication, errorStatus, errorIndex, varBinds = next(g)


    if errorIndication:
        print(errorIndication)

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))


if __name__ == "__main__":
    # get_value()
    # send_trap()
    request_one_iod()
