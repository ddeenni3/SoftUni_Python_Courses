daily_goal = int(input())

total_earned = 0

while total_earned < daily_goal:
    command = input()
    if command == 'closed':
        break
    if command == 'haircut':
        haircut_type = input()
        if haircut_type == 'mens':
            total_earned += 15
        elif haircut_type == 'ladies':
            total_earned += 20
        elif haircut_type == 'kids':
            total_earned += 10
    elif command == 'color':
        color_type = input()
        if color_type == 'touch up':
            total_earned += 20
        elif color_type == 'full color':
            total_earned += 30

if total_earned >= daily_goal:
    print(f'You have reached your target for the day!')
else:
    print(f'Target not reached! You need {abs(total_earned - daily_goal)}lv. more.')
print(f'Earned money: {total_earned}lv.')
