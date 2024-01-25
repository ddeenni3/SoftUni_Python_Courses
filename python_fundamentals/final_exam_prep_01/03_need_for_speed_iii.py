number_of_cars = int(input())

car_portfolio = []

for car in range(number_of_cars):
    car_entry = input()
    car_type, mileage, fuel = car_entry.split('|')
    car_portfolio.append({'type': car_type, 'mileage': int(mileage), 'fuel': int(fuel)})

while True:
    command = input()
    if command == 'Stop':
        break

    command = command.split(' : ')

    if command[0] == 'Drive':
        current_car = command[1]
        distance = int(command[2])
        fuel_needed = int(command[3])
        for car in car_portfolio:
            if car['type'] == current_car:
                if car['fuel'] < fuel_needed:
                    print('Not enough fuel to make that ride')
                else:
                    car['fuel'] -= fuel_needed
                    car['mileage'] += distance
                    print(f'{current_car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.')
                    if car['mileage'] >= 100000:
                        print(f'Time to sell the {current_car}!')
                        car_portfolio.remove(car)
    elif command[0] == 'Refuel':
        current_car = command[1]
        fuel_to_fill = int(command[2])
        for car in car_portfolio:
            if car['type'] == current_car:
                if car['fuel'] + fuel_to_fill > 75:
                    print(f'{current_car} refueled with {75 - car["fuel"]} liters')
                    car['fuel'] = 75
                else:
                    print(f'{current_car} refueled with {fuel_to_fill} liters')
                    car['fuel'] += fuel_to_fill
    elif command[0] == 'Revert':
        current_car = command[1]
        kilometers = int(command[2])
        for car in car_portfolio:
            if car['type'] == current_car:
                if car['mileage'] - kilometers < 10000:
                    car['mileage'] = 10000
                else:
                    car['mileage'] -= kilometers
                    print(f'{current_car} mileage decreased by {kilometers} kilometers')

for car in car_portfolio:
    print(f'{car["type"]} -> Mileage: {car["mileage"]} kms, Fuel in the tank: {car["fuel"]} lt.')
