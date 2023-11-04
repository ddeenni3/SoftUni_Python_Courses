vehicle_taxes = input().split('>>')
total_collected = 0

for vehicle in vehicle_taxes:
    current_vehicle = vehicle.split()
    vehicle_type = current_vehicle[0]
    taxing_years = int(current_vehicle[1])
    km_traveled = int(current_vehicle[2])
    total_paid = 0
    valid_car_type = True
    if vehicle_type == 'family':
        total_paid += 50 - (taxing_years * 5) + (12 * (km_traveled // 3000))
    elif vehicle_type == 'heavyDuty':
        total_paid += 80 - (taxing_years * 8) + (14 * (km_traveled // 9000))
    elif vehicle_type == 'sports':
        total_paid += 100 - (taxing_years * 9) + (18 * (km_traveled // 2000))
    else:
        valid_car_type = False
        print('Invalid car type.')
    if valid_car_type:
        print(f'A {vehicle_type} car will pay {total_paid:.2f} euros in taxes.')
        total_collected += total_paid

print(f'The National Revenue Agency will collect {total_collected:.2f} euros in taxes.')
