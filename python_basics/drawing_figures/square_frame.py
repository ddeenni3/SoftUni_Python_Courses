num = int(input())

#   printing top row + --- +

print('+', end='')
for i in range(num - 2):
    print(' -', end='')
print(' +')

#   printing middle rows | --- |
for rows in range(num - 2):
    print('|', end='')
    for columns in range(num - 2):
        print(' -', end='')
    print(' |')

#   printing bottom row + --- +
print('+', end='')
for y in range(num - 2):
    print(' -', end='')
print(' +')




