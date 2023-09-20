moves = int(input())

score = 0

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p6 = 0

for i in range(moves):
    number = int(input())
    if 0 <= number <= 9:
        score += number * 0.2
        p1 += 1
    elif 10 <= number <= 19:
        score += number * 0.3
        p2 += 1
    elif 20 <= number <= 29:
        score += number * 0.4
        p3 += 1
    elif 30 <= number <= 39:
        score += 50
        p4 += 1
    elif 40 <= number <= 50:
        score += 100
        p5 += 1
    elif number < 0 or number > 50:
        score /= 2
        p6 += 1

p1_average = p1 / moves * 100
p2_average = p2 / moves * 100
p3_average = p3 / moves * 100
p4_average = p4 / moves * 100
p5_average = p5 / moves * 100
p6_average = p6 / moves * 100


print(f'{score:.2f}')
print(f'From 0 to 9: {p1_average:.2f}%')
print(f'From 10 to 19: {p2_average:.2f}%')
print(f'From 20 to 29: {p3_average:.2f}%')
print(f'From 30 to 39: {p4_average:.2f}%')
print(f'From 40 to 50: {p5_average:.2f}%')
print(f'Invalid numbers: {p6_average:.2f}%')
