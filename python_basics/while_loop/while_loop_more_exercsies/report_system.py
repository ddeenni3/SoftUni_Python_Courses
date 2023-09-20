needed_sum = int(input())
current_sum = 0

counter = 0
counter_card = 0
counter_cash = 0

card_total = 0
cash_total = 0

while current_sum < needed_sum:
    counter += 1
    command = input()
    if command == 'End':
        break
    command = int(command)
    if counter % 2 != 0:
        if command > 100:
            print('Error in transaction!')
        else:
            counter_cash += 1
            cash_total += command
            current_sum += command
            print('Product sold!')
    else:
        if command < 10:
            print('Error in transaction!')
        else:
            counter_card += 1
            card_total += command
            current_sum += command
            print('Product sold!')

if current_sum >= needed_sum:
    print(f'Average CS: {cash_total / counter_cash:.2f}')
    print(f'Average CC: {card_total / counter_card:.2f}')
else:
    print('Failed to collect required money for charity.')
