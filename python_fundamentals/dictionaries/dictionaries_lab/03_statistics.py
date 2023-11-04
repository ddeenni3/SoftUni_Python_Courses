inventory = {}

while True:
    command = input()
    if command == 'statistics':
        break
    product, quantity = command.split(': ')
    if product in inventory.keys():
        inventory[product] += int(quantity)
    else:
        inventory[product] = int(quantity)

total_products = len(inventory)
total_quantity = sum(inventory.values())

print('Products in stock:')
for item, value in inventory.items():
    print(f'- {item}: {value}')
print(f'Total Products: {total_products}\nTotal Quantity: {total_quantity}')
