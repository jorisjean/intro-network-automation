from time import sleep

import paramiko

username = 'developer'
password = 'C1sco12345'
host = "ios-xe-mgmt-latest.cisco.com"
port = 8181

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(host, port=port, username=username, password=password, look_for_keys=False)
    channel = client.invoke_shell()

    output = channel.recv(4096)
    while not output.decode('ascii').endswith('#'):
        sleep(0.5)
    channel.send("show run | i hostname\n")
    output = channel.recv(4096)
    while not output.decode('ascii').endswith('#'):
        sleep(0.5)
        output = channel.recv(4096)
    print(output.decode('ascii'))
finally:
    client.close()
