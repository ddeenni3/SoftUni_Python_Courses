price_mackerel = float(input())
price_sprinkle = float(input())
kg_bonito = float(input())
kg_safrid = float(input())
kg_mussеls = int(input())

bonito_price = price_mackerel * 1.6
safrid_price = price_sprinkle * 1.8
mussels_price = kg_mussеls * 7.50

total_price = (bonito_price * kg_bonito) + (safrid_price * kg_safrid) + mussels_price

print(f'{total_price:.2f}')
