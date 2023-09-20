from math import ceil

tv_series = input()
episode_length = int(input())
break_length = int(input())

lunch_time = break_length * 0.125
relax_time = break_length * 0.25

time_left = break_length - lunch_time - relax_time
diff = ceil(abs(time_left-episode_length))

if time_left >= episode_length:
    print(f'You have enough time to watch {tv_series} and left with {diff} minutes free time.')
else:
    print(f"You don't have enough time to watch {tv_series}, you need {diff} more minutes.")
