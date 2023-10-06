items = input().split('|')
budget = int(input())
ticket_cost = 150
budget_left = budget

bought_items_added_price = []
total_cost = 0

for item in items:
    current_item = item.split('->')
    item_type = current_item[0]
    item_price = float(current_item[1])
    will_buy = False
    if item_type == 'Clothes' and item_price <= 50:
        will_buy = True
    elif item_type == 'Shoes' and item_price <= 35:
        will_buy = True
    elif item_type == 'Accessories' and item_price <= 20.5:
        will_buy = True
    if will_buy and budget_left - item_price >= 0:
        budget_left -= item_price
        total_cost += item_price
        item_price *= 1.4
        bought_items_added_price.append(f'{item_price:.2f}')


total_revenue = sum(list(map(float, bought_items_added_price)))
profit = total_revenue - total_cost
total_budget = profit + budget

print(' '.join(bought_items_added_price))
print(f'Profit: {profit:.2f}')
if total_budget > ticket_cost:
    print('Hello, France!')
else:
    print('Not enough money.')
