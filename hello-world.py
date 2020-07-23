print("hello world")
x = 25
y = 'toto'
list_1 = ['1', 'toto', "deux"]

for element in list_1:
    if element == y:
        print(element)

dict_1 = {
    'router1': {'version': 10, 'brand': 'cisco'},
    'router2': {'version': 20, 'brand': 'nexus'},
    'router3': {'version': 100, 'brand': 'hp'}
}

print(dict_1['router1']['version'])

for router in dict_1:
    print(dict_1[router]['brand'])

