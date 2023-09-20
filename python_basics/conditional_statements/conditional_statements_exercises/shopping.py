budget = float(input())
gpu_amount = int(input())
cpu_amount = int(input())
ram_amount = int(input())

gpu_price_total = gpu_amount * 250
cpu_price = gpu_price_total * 0.35
cpu_price_total = cpu_amount * cpu_price
ram_price = gpu_price_total * 0.10
ram_price_total = ram_amount * ram_price

total_sum = cpu_price_total + gpu_price_total + ram_price_total

if gpu_amount > cpu_amount:
    total_sum *= 0.85

diff = abs(budget - total_sum)

if budget >= total_sum:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')
