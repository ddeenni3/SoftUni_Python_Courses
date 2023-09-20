price_kg_vegetables = float(input())
price_kg_fruits = float(input())
kg_vegetables = int(input())
kg_fruits = int(input())

total_price_fruits_lv = price_kg_fruits * kg_fruits
total_price_vegetables = price_kg_vegetables * kg_vegetables
total_price_bgn = total_price_vegetables + total_price_fruits_lv

total_price_eur = total_price_bgn / 1.94

print(f'{total_price_eur:.2f}')
