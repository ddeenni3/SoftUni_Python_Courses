chrysanthemums_amount = int(input())
roses_amount = int(input())
tulips_amount = int(input())
season = input()
celebration_day = input()

chrysanthemums_cost = 0
roses_cost = 0
tulips_cost = 0

if season == 'Spring' or season == 'Summer':
    chrysanthemums_cost += chrysanthemums_amount * 2
    roses_cost += roses_amount * 4.1
    tulips_cost += tulips_amount * 2.5
elif season == 'Autumn' or season == 'Winter':
    chrysanthemums_cost += chrysanthemums_amount * 3.75
    roses_cost += roses_amount * 4.5
    tulips_cost += tulips_amount * 4.15

total_cost = chrysanthemums_cost + roses_cost + tulips_cost

if celebration_day == 'Y':
    total_cost *= 1.15
if season == 'Spring' and tulips_amount > 7:
    total_cost *= 0.95
if season == 'Winter' and roses_amount >= 10:
    total_cost *= 0.9

total_flower_amount = roses_amount + chrysanthemums_amount + tulips_amount

if total_flower_amount > 20:
    total_cost *= 0.8

total_cost += 2  # flower arrangement

print(f'{total_cost:.2f}')
