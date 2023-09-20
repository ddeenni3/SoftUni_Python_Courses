exam_starting_hour = int(input())
exam_starting_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_starting_time = exam_starting_minutes + exam_starting_hour * 60
arrival_time = arrival_minutes + arrival_hour * 60

diff = abs(exam_starting_time - arrival_time)
diff_minutes = diff % 60
diff_hours = diff // 60

if exam_starting_time == arrival_time:
    print('On time')
elif exam_starting_time > arrival_time:
    if diff <= 30:
        print(f'On time')
        print(f'{diff_minutes} minutes before the start')
    elif 30 < diff < 60:
        print('Early')
        print(f'{diff_minutes} minutes before the start')
    else:
        print('Early')
        print(f'{diff_hours}:{diff_minutes:02d} hours before the start')
elif exam_starting_time < arrival_time:
    if diff <= 30:
        print(f'Late')
        print(f'{diff_minutes} minutes after the start')
    elif 30 < diff < 60:
        print('Late')
        print(f'{diff_minutes} minutes after the start')
    else:
        print('Late')
        print(f'{diff_hours}:{diff_minutes:02d} hours after the start')
