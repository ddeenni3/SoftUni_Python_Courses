students = int(input())

excellent = 0
very_good = 0
good = 0
fail = 0
average = 0


for i in range(students):
    score = float(input())
    average += score
    if score > 4.99:
        excellent += 1
    elif score > 3.99:
        very_good += 1
    elif score > 2.99:
        good += 1
    else:
        fail += 1

excellent_average = excellent / students * 100
very_good_average = very_good / students * 100
good_average = good / students * 100
fail_average = fail / students * 100
average_score = average / students

print(f'Top students: {excellent_average:.2f}%')
print(f'Between 4.00 and 4.99: {very_good_average:.2f}%')
print(f'Between 3.00 and 3.99: {good_average:.2f}%')
print(f'Fail: {fail_average:.2f}%')
print(f'Average: {average_score:.2f}')
