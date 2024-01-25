from collections import deque
from datetime import datetime, timedelta

robots_data = input().split(';')

robots = {}

for robot in robots_data:
    name, needed_time = robot.split('-')
    robots[name] = [int(needed_time), 0]

start_time = datetime.strptime(input(), "%H:%M:%S")

products = deque()

while True:
    product = input()
    if product == 'End':
        break
    products.append(product)

while products:
    current_product = products.popleft()
    start_time += timedelta(0, 1)
    free_robots = []

    for name, value in robots.items():
        if robots[name][1] != 0:
            robots[name][1] -= 1

        if robots[name][1] == 0:
            free_robots.append([name, value])

    if not free_robots:
        products.append(current_product)
        continue

    robot_name, data = free_robots[0]
    robots[robot_name][1] = data[0]

    print(f'{robot_name} - {current_product} [{start_time.strftime("%H:%M:%S")}]')




