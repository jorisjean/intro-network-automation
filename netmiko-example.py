from netmiko import ConnectHandler

csr1000v = {
    'device_type': 'cisco_ios',
    'host':   'ios-xe-mgmt-latest.cisco.com',
    'username': 'developer',
    'password': 'C1sco12345',
    'port': 8181
}

net_connect = ConnectHandler(**csr1000v)

output = net_connect.send_command('show version')
print(output)

config_commands = [
    'interface lo100',
    'ip address 10.1.1.1 255.255.255.0',
    'description test-joris'
]
output = net_connect.send_config_set(config_commands)
print(output)
