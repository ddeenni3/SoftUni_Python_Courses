city = input()
package = input()
vip = input()
stay_length = int(input())

invalid_input = False

price = 0

if stay_length < 1:
    print(f'Days must be positive number!')
else:
    if stay_length > 7:
        stay_length -= 1
    if city == 'Bansko' or city == 'Borovets':
        if package == 'withEquipment':
            if vip == 'yes':
                price = (stay_length * 100) * 0.9
            elif vip == 'no':
                price = stay_length * 100
        elif package == 'noEquipment':
            if vip == 'yes':
                price = (stay_length * 80) * 0.95
            elif vip == 'no':
                price = stay_length * 80
        else:
            invalid_input = True
    elif city == 'Varna' or city == 'Burgas':
        if package == 'withBreakfast':
            if vip == 'yes':
                price = (stay_length * 130) * 0.88
            elif vip == 'no':
                price = stay_length * 130
        elif package == 'noBreakfast':
            if vip == 'yes':
                price = (stay_length * 100) * 0.93
            elif vip == 'no':
                price = stay_length * 100
        else:
            invalid_input = True
    else:
        invalid_input = True

    if invalid_input:
        print(f'Invalid input!')
    else:
        print(f'The price is {price:.2f}lv! Have a nice time!')
