checkpoint_times = list(map(int, input().strip().split()))
finish_line = len(checkpoint_times) // 2

first_car = checkpoint_times[:finish_line]
second_car = checkpoint_times[len(checkpoint_times) - 1:finish_line: - 1]

total_time_first_car = 0
total_time_second_car = 0

for time_first_car in first_car:
    total_time_first_car += time_first_car
    if time_first_car == 0:
        total_time_first_car *= 0.8

for time_second_car in second_car:
    total_time_second_car += time_second_car
    if time_second_car == 0:
        total_time_second_car *= 0.8

if total_time_first_car > total_time_second_car:
    print(f'The winner is right with total time: {total_time_second_car:.1f}')
else:
    print(f'The winner is left with total time: {total_time_first_car:.1f}')





