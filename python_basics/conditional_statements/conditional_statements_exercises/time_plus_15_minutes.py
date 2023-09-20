hour = int(input())
minutes = int(input())

total_time_in_minutes = minutes + hour * 60 + 15

total_hour = total_time_in_minutes // 60
total_minutes = total_time_in_minutes % 60

if total_hour > 23:
    total_hour = 0

if total_minutes < 10:
    print(f'{total_hour}:{total_minutes:02d}')
else:
    print(f'{total_hour}:{total_minutes}')
    