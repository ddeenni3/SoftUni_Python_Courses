fruit_type = input()
set_size = input()
order_qty = int(input())

price = 0

if fruit_type == 'Watermelon':
    if set_size == 'small':
        order_qty *= 2
        price = order_qty * 56
    elif set_size == 'big':
        order_qty *= 5
        price = order_qty * 28.7
elif fruit_type == 'Mango':
    if set_size == 'small':
        order_qty *= 2
        price = order_qty * 36.66
    elif set_size == 'big':
        order_qty *= 5
        price = order_qty * 19.6
elif fruit_type == 'Pineapple':
    if set_size == 'small':
        order_qty *= 2
        price = order_qty * 42.1
    elif set_size == 'big':
        order_qty *= 5
        price = order_qty * 24.8
elif fruit_type == 'Raspberry':
    if set_size == 'small':
        order_qty *= 2
        price = order_qty * 20
    elif set_size == 'big':
        order_qty *= 5
        price = order_qty * 15.2

if 400 <= price <= 1000:
    price *= 0.85
elif price > 1000:
    price *= 0.5

print(f'{price:.2f} lv.')
