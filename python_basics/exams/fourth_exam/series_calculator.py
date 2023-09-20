tv_series = input()
seasons = int(input())
episodes = int(input())
time_per_ep = float(input())

time_per_ep *= 1.2

total_series = seasons * episodes * time_per_ep + (seasons * 10)

print(f'Total time needed to watch the {tv_series} series is {round(total_series)} minutes.')
