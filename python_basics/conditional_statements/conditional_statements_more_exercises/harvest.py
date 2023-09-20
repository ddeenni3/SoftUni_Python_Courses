import math
winery_square_meters = int(input())
grapes_per_square_meters = float(input())
needed_wine_litres = int(input())
workers_amount = int(input())

total_grapes = grapes_per_square_meters * winery_square_meters
total_grapes *= 0.4
total_wine = total_grapes / 2.5
diff = abs(total_wine - needed_wine_litres)

if total_wine < needed_wine_litres:
    print(f'It will be a tough winter! More {math.floor(diff)} liters wine needed.')
else:
    wine_per_worker = diff / workers_amount
    print(f'Good harvest this year! Total wine: {math.floor(total_wine)} liters.')
    print(f'{math.ceil(diff)} liters left -> {math.ceil(wine_per_worker)} liters per person.')
