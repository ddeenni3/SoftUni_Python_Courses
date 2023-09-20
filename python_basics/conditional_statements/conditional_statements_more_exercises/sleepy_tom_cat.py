off_days_per_year = int(input())

working_days = 365 - off_days_per_year

total_play_time = off_days_per_year * 127 + working_days * 63

needed_play_time = 30000

diff = abs(total_play_time - needed_play_time)
diff_hours = diff // 60
diff_minutes = diff % 60


if total_play_time > needed_play_time:
    print('Tom will run away')
    print(f'{diff_hours} hours and {diff_minutes} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{diff_hours} hours and {diff_minutes} minutes less for play')
