money_needed = float(input())
saved_money = float(input())

spend_counter = 0
days_counter = 0

while True:
    days_counter += 1
    action = input()
    amount = float(input())
    if action == 'spend':
        spend_counter += 1
        saved_money -= amount
        if saved_money < 0:
            saved_money = 0
    elif action == 'save':
        saved_money += amount
        spend_counter = 0
    if saved_money >= money_needed:
        print(f'You saved the money for {days_counter} days.')
        break
    elif spend_counter == 5:
        print("You can't save the money.")
        print(f'{days_counter}')
        break

