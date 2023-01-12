from pysnmp.hlapi import *


def get_one_iod(value: str):

    target_value = '.1.3.6.1.4.1.40418.2.4.4.1.0'  # Name/OID: erd3temperatureSensor.0; Value (Integer): 26
    target_value2 = '.1.3.6.1.4.1.40418.2.4.4.2.2.0'  # Name/OID: erd3temperatureSensorOut1.0; Value (Integer): 21
    target_value3 = '.1.3.6.1.4.1.40418.2.4.2.3.0'  # Name/OID: erd3remoteControlContact11.0; Value (Integer): manON(0)
    target_value4 = '.1.3.6.1.4.1.40418.2.4.2.1.0'  # Name/OID: erd3resetSmartContact10.0; Value (Integer): bypass(0)

    target_value5 = '.1.3.6.1.4.1.40418.2.4.2.3.0'  # erd3remoteControlContact11

    g = getCmd(SnmpEngine(),
                CommunityData('public', mpModel=0),
                UdpTransportTarget(('192.168.1.2', 161)),
                ContextData(),
                ObjectType(ObjectIdentity(value)))

    errorIndication, errorStatus, errorIndex, varBinds = next(g)


    if errorIndication:
        print(errorIndication)

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            # print(' = '.join([x.prettyPrint() for x in varBind]))
            result = ' = '.join([x.prettyPrint() for x in varBind])

    return result


def set_one_iod(on_off: int):
    target_value5 = '.1.3.6.1.4.1.40418.2.4.2.3.0'  # erd3remoteControlContact11

    contact_off = 0
    contact_on = 1

    s = setCmd(
        SnmpEngine(),
        CommunityData('public', mpModel=0),
        UdpTransportTarget(('192.168.1.2', 161)),
        ContextData(),
        ObjectType(
            ObjectIdentity(target_value5),
            Integer(on_off)

    ))

    errorIndication, errorStatus, errorIndex, varBinds = next(s)

    if errorIndication:
        print(errorIndication)

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))

#
# if __name__ == "__main__":
#     # get_one_iod()
#     set_one_iod()
