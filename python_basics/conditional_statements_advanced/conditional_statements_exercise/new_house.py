flower_type = input()
amount_of_flowers = int(input())
budget = int(input())

roses_price = 5
dahlia_price = 3.8
tulip_price = 2.80
narcissus_price = 3
gladiolus_price = 2.5

total_price = 0

if flower_type == 'Roses':
    total_price = amount_of_flowers * roses_price
    if amount_of_flowers > 80:
        total_price *= 0.9
if flower_type == 'Dahlias':
    total_price = amount_of_flowers * dahlia_price
    if amount_of_flowers > 90:
        total_price *= 0.85
if flower_type == 'Tulips':
    total_price = amount_of_flowers * tulip_price
    if amount_of_flowers > 80:
        total_price *= 0.85
if flower_type == 'Narcissus':
    total_price = amount_of_flowers * narcissus_price
    if amount_of_flowers < 120:
        total_price *= 1.15
if flower_type == 'Gladiolus':
    total_price = amount_of_flowers * gladiolus_price
    if amount_of_flowers < 80:
        total_price *= 1.20

diff = abs(budget - total_price)

if budget >= total_price:
    print(f'Hey, you have a great garden with {amount_of_flowers} {flower_type} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')
