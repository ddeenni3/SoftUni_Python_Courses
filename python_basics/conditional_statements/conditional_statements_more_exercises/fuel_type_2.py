fuel_type = input()
fuel_amount = float(input())
discount_card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

total_price = 0

if discount_card == 'Yes':
    gasoline_price -= 0.18
    diesel_price -= 0.12
    gas_price -= 0.08

if fuel_type == 'Gasoline':
    total_price = fuel_amount * gasoline_price
elif fuel_type == 'Diesel':
    total_price = fuel_amount * diesel_price
elif fuel_type == 'Gas':
    total_price = fuel_amount * gas_price

if 20 <= fuel_amount <= 25:
    total_price *= 0.92
elif fuel_amount > 25:
    total_price *= 0.90

print(f'{total_price:.2f} lv.')

