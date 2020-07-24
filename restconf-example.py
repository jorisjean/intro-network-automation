import requests

username = 'developer'
password = 'C1sco12345'
host = "ios-xe-mgmt-latest.cisco.com"
port = '9443'


#url = "https://" + host + ":" + port + "/restconf/data/ietf-interfaces:interfaces/interface"
url = "https://" + host + ":" + port + "/restconf/data/Cisco-IOS-XE-native:native/interface"

headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}
response = requests.request("GET", url, headers=headers, auth=(username, password), verify=False)

print(response.json())

for type in response.json()['Cisco-IOS-XE-native:interface']:
    for interface in response.json()['Cisco-IOS-XE-native:interface'][type]:
        print(f"{type}{interface['name']}")




url = f"https://{host}:{port}/restconf/data/Cisco-IOS-XE-native:native/hostname"
response = requests.request("GET", url, headers=headers, auth=(username, password), verify=False)
print(response.json())

payload = "{\"hostname\": \"TestName2\"}"
url = f"https://{host}:{port}/restconf/data/Cisco-IOS-XE-native:native/hostname"
response = requests.request("PUT", url, headers=headers, data=payload, auth=(username, password), verify=False)
print(response)

url = f"https://{host}:{port}/restconf/data/Cisco-IOS-XE-native:native/hostname"
response = requests.request("GET", url, headers=headers, auth=(username, password), verify=False)
print(response.json())