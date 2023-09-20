number = int(input('Number =:'))
number1 = number
result = 0
print1 = ''


while True:
    result = number1 % 2
    print1 += f'{result}'
    decline = number1 // 2
    number1 = decline
    if number1 < 1:
        print(print1[::-1])
        break


    #     if number < 1:
    #         print(print1[::-1])
    #         break
    # else:
    #     result = number % 2
    #     print1 += f'{result}'
    #     decline = number // 2
    #     number = decline
    #     if number < 1:
    #         print(print1)
    #         break



