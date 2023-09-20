puzzle_price = 2.60
talking_doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

vacation_cost = float(input())
amount_of_puzzles = int(input())
amount_of_talking_dolls = int(input())
amount_of_teddy_bears = int(input())
amount_of_minions = int(input())
amount_of_trucks = int(input())

total_sum = amount_of_trucks * truck_price + amount_of_minions * minion_price + \
            amount_of_puzzles * puzzle_price + amount_of_teddy_bears * teddy_bear_price + \
            amount_of_talking_dolls * talking_doll_price

total_amount = amount_of_trucks + amount_of_minions + amount_of_puzzles\
               + amount_of_talking_dolls + amount_of_teddy_bears

if total_amount >= 50:
    total_sum *= 0.75

total_sum *= 0.9

diff = total_sum - vacation_cost

if diff >= 0:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {abs(diff):.2f} lv needed.')