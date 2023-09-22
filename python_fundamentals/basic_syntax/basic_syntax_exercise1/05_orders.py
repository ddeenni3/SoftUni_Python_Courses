number_of_orders = int(input())

total = 0


for order in range(number_of_orders):

    price_per_capsule = float(input())
    days = int(input())
    needed_capsules_per_day = int(input())
    if needed_capsules_per_day < 1 or needed_capsules_per_day > 2000:
        continue
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    bill = (needed_capsules_per_day * price_per_capsule) * days

    print(f'The price for the coffee is: ${bill:.2f}')
    total += bill

print(f'Total: ${total:.2f}')
