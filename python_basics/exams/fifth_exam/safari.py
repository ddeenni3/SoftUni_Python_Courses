budget = float(input())
needed_fuel_litres = float(input())
day_of_week = input()

fuel_price = needed_fuel_litres * 2.1
guide = 100

total = fuel_price + guide

if day_of_week == 'Saturday':
    total *= 0.9
elif day_of_week == 'Sunday':
    total *= 0.8

diff = abs(total - budget)

if total > budget:
    print(f'Not enough money! Money needed: {diff:.2f} lv.')
else:
    print(f'Safari time! Money left: {diff:.2f} lv. ')
    