number_of_points = int(input())
bonus = 0

if number_of_points <= 100:
    bonus += 5
elif number_of_points > 1000:
    bonus = number_of_points * 0.1
else:
    bonus = number_of_points * 0.2

if number_of_points % 2 == 0:
    bonus += 1
elif number_of_points % 10 == 5:
    bonus += 2

total_points = number_of_points + bonus

print(bonus)
print(total_points)
