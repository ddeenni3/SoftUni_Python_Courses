price_luggage_above_20kg = float(input())
luggage_weight = float(input())
days = int(input())
bags_qty = int(input())

price = 0

if luggage_weight < 10:
    price = bags_qty * (price_luggage_above_20kg * 0.2)
elif luggage_weight <= 20:
    price = bags_qty * (price_luggage_above_20kg * 0.5)
else:
    price = bags_qty * price_luggage_above_20kg

if days < 7:
    price *= 1.4
elif days <= 30:
    price *= 1.15
else:
    price *= 1.1

print(f'The total price of bags is: {price:.2f} lv. ')
