inventory = {}

while True:
    command = input()
    if command == 'buy':
        break
    name, price, quantity = command.split()
    if name not in inventory.keys():
        inventory[name] = {'price': float(price), 'quantity': int(quantity)}
    else:
        inventory[name]['price'] = float(price)
        inventory[name]['quantity'] += int(quantity)
for product, value in inventory.items():
    for price, quantity in value.items():
        total = value['price'] * value['quantity']
        inventory[product] = total
        break

for product, value in inventory.items():
    print(f'{product} -> {value:.2f}')
