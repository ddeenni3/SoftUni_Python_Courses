strawberries_price = float(input())
banana_kgs = float(input())
oranges_kgs = float(input())
raspberries_kgs = float(input())
strawberries_kgs = float(input())

total_strawberries = strawberries_kgs * strawberries_price
raspberries_price = strawberries_price * 0.5
total_raspberries = raspberries_kgs * raspberries_price
oranges_price = raspberries_price * 0.6
total_oranges = oranges_kgs * oranges_price
bananas_price = raspberries_price * 0.2
total_bananas = banana_kgs * bananas_price

total_price = total_bananas + total_oranges + total_raspberries + total_strawberries

print(f'{total_price:.2f}')