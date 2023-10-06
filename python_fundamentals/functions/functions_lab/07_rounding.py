def numbers_rounding(n):
    return round(n)


numbers = list(map(float, input().split()))

rounded = []

for num in numbers:
    rounded.append(numbers_rounding(num))

print(rounded)