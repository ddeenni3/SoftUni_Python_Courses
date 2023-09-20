junior_amount = int(input())
senior_amount = int(input())
trail_type = input()

junior_price = 0
senior_price = 0
total_cost = 0

if trail_type == 'trail':
    junior_price += junior_amount * 5.5
    senior_price += senior_amount * 7
elif trail_type == 'cross-country':
    junior_price += junior_amount * 8
    senior_price += senior_amount * 9.5
    if junior_amount + senior_amount >= 50:
        junior_price *= 0.75
        senior_price *= 0.75
elif trail_type == 'downhill':
    junior_price += junior_amount * 12.25
    senior_price += senior_amount * 13.75
elif trail_type == 'road':
    junior_price += junior_amount * 20
    senior_price += senior_amount * 21.5

total_cost = junior_price + senior_price
total_cost *= 0.95  # other costs 5%

print(f'{total_cost:.2f}')
