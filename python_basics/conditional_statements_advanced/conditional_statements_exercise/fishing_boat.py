budget = int(input())
season = input()
fisherman_amount = int(input())

rental_price = 0

if season == 'Spring':
    rental_price += 3000
elif season == 'Summer' or season == 'Autumn':
    rental_price += 4200
elif season == 'Winter':
    rental_price += 2600

if fisherman_amount <= 6:
    rental_price *= 0.9
elif 6 < fisherman_amount <= 11:
    rental_price *= 0.85
elif fisherman_amount >= 12:
    rental_price *= 0.75

if season != 'Autumn' and fisherman_amount % 2 == 0:
    rental_price *= 0.95

diff = abs(budget - rental_price)

if budget >= rental_price:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')
