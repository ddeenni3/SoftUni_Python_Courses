packages_amount = int(input())

tones = 0
price_per_tone = 0
bus = 0
truck = 0
train = 0

for i in range(packages_amount):
    package_weight = int(input())
    tones += package_weight
    if package_weight <= 3:
        bus += package_weight
        price_per_tone += package_weight * 200
    elif package_weight <= 11:
        truck += package_weight
        price_per_tone += package_weight * 175
    else:
        train += package_weight
        price_per_tone += package_weight * 120

average_price = price_per_tone / tones
truck_amount = truck / tones * 100
bus_amount = bus / tones * 100
train_amount = train / tones * 100

print(f'{average_price:.2f}')
print(f'{bus_amount:.2f}%')
print(f'{truck_amount:.2f}%')
print(f'{train_amount:.2f}%')
