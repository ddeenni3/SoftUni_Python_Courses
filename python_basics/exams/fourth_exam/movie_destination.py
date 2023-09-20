budget = float(input())
destination = input()
season = input()
days = int(input())

price = 0

if season == 'Winter':
    if destination == 'Dubai':
        price += days * 45000
    elif destination == 'Sofia':
        price += days * 17000
    elif destination == 'London':
        price += days * 24000
elif season == 'Summer':
    if destination == 'Dubai':
        price += days * 40000
    elif destination == 'Sofia':
        price += days * 12500
    elif destination == 'London':
        price += days * 20250

if destination == 'Dubai':
    price *= 0.7
if destination == 'Sofia':
    price *= 1.25

diff = abs(price - budget)

if price <= budget:
    print(f'The budget for the movie is enough! We have {diff:.2f} leva left!')
else:
    print(f'The director needs {diff:.2f} leva more!')