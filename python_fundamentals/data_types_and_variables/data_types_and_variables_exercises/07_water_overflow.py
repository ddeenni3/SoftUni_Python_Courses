water_tank_capacity = 255
number = int(input())
total = 0
for _ in range(number):
    litres_to_pour = int(input())
    total += litres_to_pour
    if total > water_tank_capacity:
        print('Insufficient capacity!')
        total -= litres_to_pour
        continue
print(total)
