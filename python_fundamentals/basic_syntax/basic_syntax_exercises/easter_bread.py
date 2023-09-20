budget = float(input())
kg_flour_price = float(input())
eggs_price = kg_flour_price * 0.75
quarter_milk_price = kg_flour_price * 1.25 / 4
loaf_price = kg_flour_price + eggs_price + quarter_milk_price
loaf_counter = 0
eggs_counter = 0

while budget >= loaf_price:
    loaf_counter += 1
    eggs_counter += 3
    budget -= loaf_price
    if loaf_counter % 3 == 0:
        eggs_counter -= loaf_counter - 2

print(f'You made {loaf_counter} loaves of Easter bread! Now you have {eggs_counter} eggs and {budget:.2f}BGN left.')

