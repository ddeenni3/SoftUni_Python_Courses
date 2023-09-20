money = float(input())
year_to_live = int(input())


years_alive = year_to_live - 1800

years_old = 18

for i in range(years_alive + 1):

    if i % 2 == 0:
        money -= 12000
    else:
        money -= 12000 + 50 * years_old
    years_old += 1

if money >= 0:
    print(f'Yes! He will live a carefree life and will have {money:.2f} dollars left.')
else:
    money = abs(money)
    print(f'He will need {money:.2f} dollars to survive.')
