stadium_capacity = int(input())
supporters_amount = int(input())

first_team = 0
second_team = 0

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for i in range(supporters_amount):
    sector = input()
    if sector == 'A':
        sector_a += 1
        first_team += 1
    elif sector == 'B':
        sector_b += 1
        first_team += 1
    elif sector == 'V':
        sector_v += 1
        second_team += 1
    elif sector == 'G':
        sector_g += 1
        second_team += 1


sector_a_avg = sector_a / supporters_amount * 100
sector_b_avg = sector_b / supporters_amount * 100
sector_v_avg = sector_v / supporters_amount * 100
sector_g_avg = sector_g / supporters_amount * 100
fans_avg = supporters_amount / stadium_capacity * 100

print(f'{sector_a_avg:.2f}%')
print(f'{sector_b_avg:.2f}%')
print(f'{sector_v_avg:.2f}%')
print(f'{sector_g_avg:.2f}%')
print(f'{fans_avg:.2f}%')
