years = int(input())
machine_price = float(input())
toy_price = int(input())

money = 0
money_2nd_year = 10

for i in range(1, years + 1):
    if i % 2 == 0:
        money += money_2nd_year
        money -= 1
        money_2nd_year += 10
    else:
        money += toy_price

diff = abs(money - machine_price)

if money >= machine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
