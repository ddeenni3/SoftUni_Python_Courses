number_of_commands = [input().split(', ') for _ in range(int(input()))]

parking_lot = set()

for command in number_of_commands:
    direction, car_plate = command[0], command[1]
    if direction == 'IN':
        parking_lot.add(car_plate)
    elif direction == 'OUT':
        parking_lot.remove(car_plate)

if parking_lot:
    print(*parking_lot, sep='\n')
else:
    print('Parking Lot is Empty')