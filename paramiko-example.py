import paramiko

username = 'developer'
password = 'C1sco12345'
host = "10.10.20.48"
port = 22


try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(host, port=port, username=username, password=password, look_for_keys=False)

    stdin, stdout, stderr = client.exec_command("show version")
    print(stdout.read())

finally:
    client.close()