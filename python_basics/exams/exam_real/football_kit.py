t_shirt_price = float(input())
sum_needed = float(input())

short_price = t_shirt_price * 0.75
socks_price = short_price * 0.2
shoes = 2 * (short_price + t_shirt_price)

total = t_shirt_price + shoes + short_price + socks_price

total *= 0.85

if total >= sum_needed:
    print(f'Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {total:.2f} lv.')
else:
    print(f'No, he will not earn the world-cup replica ball.')
    print(f'He needs {abs(total - sum_needed):.2f} lv. more.')
