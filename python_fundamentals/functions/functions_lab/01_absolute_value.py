def abs_value(n):
    return abs(n)


numbers = list(map(float, input().split()))

abs_numbers = []

for num in numbers:
    abs_numbers.append(abs_value(num))

print(abs_numbers)
