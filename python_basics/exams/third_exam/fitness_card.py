budget = float(input())
sex = input()
age = int(input())
sport = input()

card_price = 0

if sex == 'm':
    if sport == 'Gym':
        card_price += 42
    elif sport == 'Boxing':
        card_price += 41
    elif sport == 'Yoga':
        card_price += 45
    elif sport == 'Zumba':
        card_price += 34
    elif sport == 'Dances':
        card_price += 51
    elif sport == 'Pilates':
        card_price += 39
elif sex == 'f':
    if sport == 'Gym':
        card_price += 35
    elif sport == 'Boxing':
        card_price += 37
    elif sport == 'Yoga':
        card_price += 42
    elif sport == 'Zumba':
        card_price += 31
    elif sport == 'Dances':
        card_price += 53
    elif sport == 'Pilates':
        card_price += 37
if age < 20:
    card_price *= 0.8

diff = abs(budget - card_price)

if budget >= card_price:
    print(f'You purchased a 1 month pass for {sport}.')
else:
    print(f'You don\'t have enough money! You need ${diff:.2f} more.')

