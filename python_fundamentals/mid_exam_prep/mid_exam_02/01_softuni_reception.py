employee_one_per_hour = int(input())
employee_two_per_hour = int(input())
employee_three_per_hour = int(input())
students_amount = int(input())

total_students_per_hour = employee_one_per_hour + employee_two_per_hour + employee_three_per_hour

hours_needed = 0

while students_amount > 0:
    students_amount -= total_students_per_hour
    hours_needed += 1
    if hours_needed % 4 == 0:
        hours_needed += 1
        continue

print(f'Time needed: {hours_needed}h.')