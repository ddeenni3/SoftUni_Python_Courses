budget = float(input())
flour_kg_price = float(input())
eggs_pack_price = flour_kg_price * 0.75
milk_litre_price = (flour_kg_price * 1.25) * 0.25

price_per_loaf = flour_kg_price + eggs_pack_price + milk_litre_price

loaf_counter = 0

colored_eggs = 0

while True:
    if (budget - price_per_loaf) < 0:
        break
    budget -= price_per_loaf
    loaf_counter += 1
    colored_eggs += 3
    if loaf_counter % 3 == 0:
        colored_eggs -= loaf_counter - 2

print(f'You made {loaf_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
