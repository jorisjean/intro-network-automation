from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    username='developer',
    password='C1sco12345',
    host="ios-xe-mgmt-latest.cisco.com",
    port='10000',
    device_params={'name': "csr"}
)

hostname_filter = '''
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname></hostname>
    </native>
</filter>
                  '''

raw_output = m.get_config('running', hostname_filter)
print(raw_output)
xmlDom = xml.dom.minidom.parseString(str(raw_output))
print(xmlDom.toprettyxml(indent="  "))

data = '''
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>CSR1000v</hostname>
    </native>
</config>
'''

raw_output = m.edit_config(data, target='running')
xmlDom = xml.dom.minidom.parseString(str(raw_output))
print(xmlDom.toprettyxml(indent="  "))