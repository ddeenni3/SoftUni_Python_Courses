n = int(input())

counter = 0

for i in range(n):
    num = int(input())
    counter += num

print(f'{counter / n:.2f}')
