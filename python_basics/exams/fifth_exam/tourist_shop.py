budget = float(input())

total_price = 0
counter = 0

while True:
    command = input()
    if command == 'Stop':
        print(f'You bought {counter} products for {total_price:.2f} leva.')
        break
    product_price = float(input())

    counter += 1
    if counter % 3 == 0:
        product_price *= 0.5
    budget -= product_price
    if budget < 0:
        print(f'You don\'t have enough money!')
        print(f'You need {abs(budget):.2f} leva!')
        break
    total_price += product_price


