water_tank_capacity = 255

number = int(input())

counter = 0
total = 0

for _ in range(number):
    litres_to_pour = int(input())
    is_full = False
    total += litres_to_pour
    counter += 1
    if total > 255:
        print('Insufficient capacity!')
        is_full = True
        total -= litres_to_pour
        continue

print(total)