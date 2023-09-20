saved_money = 0

while True:
    destination = input()
    if destination == 'End':
        break
    needed_money = float(input())
    while saved_money < needed_money:
        current_sum = float(input())
        saved_money += current_sum
        if saved_money >= needed_money:
            print(f'Going to {destination}!')
            saved_money = 0
            break


