travel_distance = int(input())
time = input()
travel_expenses = 0

if travel_distance < 20:
    if time == 'day':
        travel_expenses = 0.79 * travel_distance + 0.70
    elif time == 'night':
        travel_expenses = 0.90 * travel_distance + 0.70
elif 20 <= travel_distance < 100:
    travel_expenses = 0.09 * travel_distance
else:
    travel_expenses = 0.06 * travel_distance

print(f'{travel_expenses:.2f}')
