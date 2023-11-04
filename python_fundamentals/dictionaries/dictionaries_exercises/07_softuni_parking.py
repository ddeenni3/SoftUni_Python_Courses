def register(some_name: str, some_car_plate: str):
    if some_name in parking_lot.keys():
        print(f'ERROR: already registered with plate number {some_car_plate}')
    else:
        parking_lot[some_name] = some_car_plate
        print(f'{some_name} registered {some_car_plate} successfully')


def unregister(some_name: str):
    if some_name not in parking_lot.keys():
        print(f'ERROR: user {some_name} not found')
    else:
        parking_lot.pop(some_name)
        print(f'{name} unregistered successfully')


number_of_commands = int(input())
parking_lot = {}

for current_command in range(number_of_commands):
    operation, *items = input().split()
    if operation == 'register':
        name = items[0]
        car_plate = items[1]
        register(name, car_plate)
    elif operation == 'unregister':
        name = items[0]
        unregister(name)

for name, car_plate_num in parking_lot.items():
    print(f'{name} => {car_plate_num}')
