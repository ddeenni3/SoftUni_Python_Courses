service = input()
distance = float(input())

price = 0

if service == 'express':
    if distance < 1:
        price = distance * 0.03
        express_price = price * 0.08 + price
        total = distance * express_price

print(f'{total:.3f}')
