hundreds_interval_end = int(input())
tens_interval_end = int(input())
ones_interval_end = int(input())

num1 = 0
num2 = 0
num3 = 0

for ones in range(1, hundreds_interval_end + 1):
    if ones % 2 != 0:
        continue
    else:
        num1 = ones
        for tens in range(2, tens_interval_end + 1):
            is_prime = True
            for num in range(2, tens):
                if tens % num == 0:
                    is_prime = False
                    break
            if not is_prime:
                continue
            else:
                num2 = tens
            for hundreds in range(1, ones_interval_end + 1):
                if hundreds % 2 != 0:
                    continue
                else:
                    num3 = hundreds
                    print(f'{num1} {num2} {num3}')
