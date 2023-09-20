minutes_per_walk = int(input())
walks_per_day = int(input())
calories_eaten = int(input())

total_minutes = walks_per_day * minutes_per_walk
total_calories = total_minutes * 5

if total_calories >= calories_eaten / 2:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {total_calories}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {total_calories}.')

