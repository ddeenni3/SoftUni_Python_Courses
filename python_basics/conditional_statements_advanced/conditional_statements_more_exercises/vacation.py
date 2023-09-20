budget = float(input())
season = input()

location = ''
accommodation = ''
cost = 0

if budget <= 1000:
    accommodation = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        cost += budget * 0.65
    elif season == 'Winter':
        location = 'Morocco'
        cost += budget * 0.45
elif 1000 < budget <= 3000:
    accommodation = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        cost += budget * 0.8
    elif season == 'Winter':
        location = 'Morocco'
        cost += budget * 0.6
else:
    accommodation = 'Hotel'
    cost += budget * 0.9
    if season == 'Summer':
        location = 'Alaska'
    elif season == 'Winter':
        location = 'Morocco'

print(f'{location} - {accommodation} - {cost:.2f}')
