shooting_time = int(input())
scenes_qty = int(input())
time_per_scene = int(input())

shooting_time *= 0.85

time_needed = scenes_qty * time_per_scene

diff = abs(time_needed - shooting_time)

if time_needed <= shooting_time:
    print(f'You managed to finish the movie on time! You have {round(diff)} minutes left!')
else:
    print(f'Time is up! To complete the movie you need {round(diff)} minutes.')
