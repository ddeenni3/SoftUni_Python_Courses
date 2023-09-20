budget = float(input())
series_qty = int(input())

total_price = 0

for i in range(series_qty):
    tv_series = input()
    price = float(input())
    if tv_series == 'Thrones':
        price *= 0.5
    elif tv_series == 'Lucifer':
        price *= 0.6
    elif tv_series == 'Protector':
        price *= 0.7
    elif tv_series == 'TotalDrama':
        price *= 0.8
    elif tv_series == 'Area':
        price *= 0.9
    total_price += price

diff = abs(total_price - budget)

if total_price <= budget:
    print(f'You bought all the series and left with {diff:.2f} lv.')
else:
    print(f'You need {diff:.2f} lv. more to buy the series!')

