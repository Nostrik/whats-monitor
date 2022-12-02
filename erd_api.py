from pysnmp.hlapi import *
from pysnmp.entity.rfc3413.oneliner import cmdgen

if __name__ == "__main__":
    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd(
        cmdgen.CommunityData('XFiles'),
        cmdgen.UdpTransportTarget(('172.18.114.6', 161)),
        '1.3.6.1.2.1.17.7.1.2.2.1.2'
    )

    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBindTable[-1][int(errorIndex) - 1] or '?'
            )
                  )
        else:
            for varBindTableRow in varBindTable:
                for name, val in varBindTableRow:
                    print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
