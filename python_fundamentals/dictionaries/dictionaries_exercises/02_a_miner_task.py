resources = {}

while True:
    resource = input()
    if resource == 'stop':
        break
    quantity = int(input())
    if resource not in resources.keys():
        resources[resource] = quantity
    else:
        resources[resource] += quantity

for resource, quantity in resources.items():
    print(f'{resource} -> {quantity}')
