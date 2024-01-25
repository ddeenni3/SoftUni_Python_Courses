from collections import deque

total_food = int(input())

orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    current_order = orders.popleft()
    if total_food >= current_order:
        total_food -= current_order
    else:
        orders.appendleft(current_order)
        print(f'Orders left:', *orders)
        break
else:
    print('Orders complete')
