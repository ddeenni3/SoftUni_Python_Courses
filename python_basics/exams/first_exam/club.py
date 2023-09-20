needed_money = input()
current_money = 0

break_flag = False

while True:
    needed_money = float(needed_money)
    cocktail_name = input()
    while True:
        if cocktail_name == 'Party!':
            break_flag = True
            break
        amount = int(input())
        cocktail_price = len(cocktail_name) * amount
        if cocktail_price % 2 != 0:
            cocktail_price *= 0.75
        current_money += cocktail_price
        if current_money >= needed_money:
            break_flag = True
            break
        cocktail_name = input()
    if break_flag:
        break


diff = abs(float(needed_money) - current_money)

if current_money >= float(needed_money):
    print('Target acquired.')
else:
    print(f'We need {diff:.2f} leva more.')
print(f'Club income - {current_money:.2f} leva.')




