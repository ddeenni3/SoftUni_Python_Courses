month = input()
stay_length = int(input())

studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
    studio_price += stay_length * 50
    apartment_price += stay_length * 65
    if 7 < stay_length < 14:
        studio_price *= 0.95
    elif stay_length > 14:
        studio_price *= 0.7
elif month == 'June' or month == 'September':
    studio_price += stay_length * 75.2
    apartment_price += stay_length * 68.7
    if stay_length > 14:
        studio_price *= 0.8
elif month == 'July' or month == 'August':
    studio_price += stay_length * 76
    apartment_price += stay_length * 77

if stay_length > 14:
    apartment_price *= 0.9

print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')
