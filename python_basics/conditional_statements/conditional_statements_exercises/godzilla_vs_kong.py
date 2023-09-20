budget = float(input())
extras = int(input())
price_per_extra_clothes = float(input())

decorations = budget * 0.1
price_for_extra_clothes = extras * price_per_extra_clothes

if extras > 150:
    price_for_extra_clothes *= 0.9

total_cost = price_for_extra_clothes + decorations

diff = abs(budget - total_cost)

if budget >= total_cost:
    print('Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')
