movie = input()
package = input()
tickets = int(input())

price = 0

if movie == 'John Wick':
    if package == 'Drink':
        price = tickets * 12
    elif package == 'Popcorn':
        price = tickets * 15
    elif package == 'Menu':
        price = tickets * 19
elif movie == 'Star Wars':
    if package == 'Drink':
        price = tickets * 18
    elif package == 'Popcorn':
        price = tickets * 25
    elif package == 'Menu':
        price = tickets * 30
elif movie == 'Jumanji':
    if package == 'Drink':
        price = tickets * 9
    elif package == 'Popcorn':
        price = tickets * 11
    elif package == 'Menu':
        price = tickets * 14

if movie == 'Star Wars' and tickets >= 4:
    price *= 0.7
if movie == 'Jumanji' and tickets == 2:
    price *= 0.85

print(f'Your bill is {price:.2f} leva.')
