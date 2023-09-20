voucher_value = int(input())

command = input()

tickets = 0
others = 0

while command != 'End' and voucher_value > 0:
    if len(command) > 8:
        price1 = ord(command[0]) + ord(command[1])
        if price1 > voucher_value:
            break
        voucher_value -= price1
        tickets += 1
    else:
        price2 = ord(command[0])
        if price2 > voucher_value:
            break
        voucher_value -= price2
        others += 1
    command = input()


print(f'{tickets}')
print(f'{others}')
