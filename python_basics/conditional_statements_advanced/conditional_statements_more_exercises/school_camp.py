season = input()
group_type = input()
students_amount = int(input())
stay_length = int(input())

cost = 0
sport = ''

if season == 'Winter':
    if group_type == 'boys':
        cost += (students_amount * 9.6) * stay_length
        sport = 'Judo'
    elif group_type == 'girls':
        cost += (students_amount * 9.6) * stay_length
        sport = 'Gymnastics'
    elif group_type == 'mixed':
        cost += (students_amount * 10) * stay_length
        sport = 'Ski'
elif season == 'Spring':
    if group_type == 'boys':
        cost += (students_amount * 7.2) * stay_length
        sport = 'Tennis'
    elif group_type == 'girls':
        cost += (students_amount * 7.2) * stay_length
        sport = 'Athletics'
    elif group_type == 'mixed':
        cost += (students_amount * 9.5) * stay_length
        sport = 'Cycling'
elif season == 'Summer':
    if group_type == 'boys':
        cost += (students_amount * 15) * stay_length
        sport = 'Football'
    elif group_type == 'girls':
        cost += (students_amount * 15) * stay_length
        sport = 'Volleyball'
    elif group_type == 'mixed':
        cost += (students_amount * 20) * stay_length
        sport = 'Swimming'

if students_amount >= 50:
    cost *= 0.5
elif 20 <= students_amount < 50:
    cost *= 0.85
elif 10 <= students_amount < 20:
    cost *= 0.95

print(f'{sport} {cost:.2f} lv.')
