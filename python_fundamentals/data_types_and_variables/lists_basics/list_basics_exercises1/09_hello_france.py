collection_of_items = input().split('|')
starting_budget = int(input())
current_budget = starting_budget
ticket_price = 150

items_sold_prices = []

for item in collection_of_items:
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
    if will_buy and current_budget - item_price >= 0:
        current_budget -= item_price
        item_price *= 1.4
        items_sold_prices.append(item_price)

total_revenue = sum(items_sold_prices)
total_cost = starting_budget - current_budget
profit = total_revenue - total_cost

for item in items_sold_prices:
    print(f'{item:.2f}', end=' ')

print(f'\nProfit: {profit:.2f}')
if total_revenue + current_budget > ticket_price:
    print('Hello, France!')
else:
    print('Not enough money.')
