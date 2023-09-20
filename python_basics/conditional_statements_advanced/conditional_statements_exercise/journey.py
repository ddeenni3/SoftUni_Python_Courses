budget = float(input())
season = input()

travel_expense = 0
accommodation = 'Hotel'
destination = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        accommodation = 'Camp'
        travel_expense += budget * 0.3
    elif season == 'winter':
        travel_expense += budget * 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        travel_expense += budget * 0.4
        accommodation = 'Camp'
    elif season == 'winter':
        travel_expense += budget * 0.8
elif budget > 1000:
    destination = 'Europe'
    travel_expense += budget * 0.9

print(f'Somewhere in {destination}')
print(f'{accommodation} - {travel_expense:.2f}')

