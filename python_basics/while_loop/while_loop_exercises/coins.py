total_sum = float(input())

coins = 0

while total_sum > 0:
    if total_sum >= 2:
        total_sum -= 2
        coins += 1
    elif total_sum >= 1:
        total_sum -= 1
        coins += 1
    elif total_sum >= 0.5:
        total_sum -= 0.5
        coins += 1
    elif total_sum >= 0.2:
        total_sum -= 0.2
        coins += 1
    elif total_sum >= 0.1:
        total_sum -= 0.1
        coins += 1
    elif total_sum >= 0.05:
        total_sum -= 0.05
        coins += 1
    elif total_sum >= 0.02:
        total_sum -= 0.02
        coins += 1
    elif total_sum >= 0.01:
        total_sum -= 0.01
        coins += 1
    total_sum = round(total_sum, 2)
print(f'{coins}')

