import re

pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'

products = []
costs = 0

while True:
    command = input()
    if command == 'Purchase':
        break
    match = re.search(pattern, command)
    if match:
        product, price, quantity = match.group(1), match.group(2), match.group(3)
        products.append(product)
        costs += float(price) * int(quantity)

print('Bought furniture:')
for product in products:
    print(product)
print(f'Total money spend: {costs:.2f}')
