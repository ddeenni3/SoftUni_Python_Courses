pack_of_pens = 5.80
pack_of_markers = 7.20
cleaning_chemical = 1.20

number_packs_of_pen = int(input())
number_packs_of_markers = int(input())
litres_cleaning_chemical = int(input())
discount = int(input())
discount /= 100

price_for_pens = number_packs_of_pen * pack_of_pens
price_for_markers = number_packs_of_markers * pack_of_markers
price_for_cleaning_chem = litres_cleaning_chemical * cleaning_chemical

total_price = price_for_pens + price_for_markers + price_for_cleaning_chem
discount_price = total_price - total_price * discount

print(discount_price)


