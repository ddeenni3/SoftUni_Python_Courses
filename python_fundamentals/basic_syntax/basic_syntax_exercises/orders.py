number_of_orders = int(input())

total_price = 0

for order in range(number_of_orders):
    price_per_coffee_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if capsules_needed_per_day < 1 or capsules_needed_per_day > 2000:
        continue
    if price_per_coffee_capsule < 0.01 or price_per_coffee_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    current_price = days * capsules_needed_per_day * price_per_coffee_capsule
    print(f'The price for the coffee is: ${current_price:.2f}')
    total_price += current_price

print(f'Total: ${total_price:.2f}')
