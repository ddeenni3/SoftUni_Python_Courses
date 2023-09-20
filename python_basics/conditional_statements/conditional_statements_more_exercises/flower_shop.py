import math

magnolias_price = 3.25
hyacinths_price = 4
roses_price = 3.5
cactus_price = 8

magnolias_amount = int(input())
hyacinths_amount = int(input())
roses_amount = int(input())
cactus_amount = int(input())
gift_price = float(input())

total_sum = magnolias_amount * magnolias_price + hyacinths_amount * hyacinths_price \
            + roses_amount * roses_price + cactus_amount * cactus_price
total_sum *= 0.95  # tax

diff = abs(total_sum - gift_price)

if total_sum >= gift_price:
    print(f'She is left with {math.floor(diff)} leva.')
else:
    print(f'She will have to borrow {math.ceil(diff)} leva.')
