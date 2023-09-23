number = int(input())

for i in range(number):
    for b in range(number):
        for y in range(number):
            print(f'{chr(97 + i)}{chr(97 +b)}{chr(97 + y)}')
