number = int(input())

for num in range(1111, 10000):
    is_special = True
    current_number = str(num)
    for i in range(len(current_number)):
        n1 = int(current_number[i])
        if n1 == 0 or number % n1 != 0:
            is_special = False
            break

    if is_special:
        print(current_number, end=' ')
    else:
        is_special = True
