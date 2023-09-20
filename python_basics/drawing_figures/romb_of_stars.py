n = int(input())

#   upper part

for row in range(1, n + 1):
    for _ in range(1, n - row + 1):
        print(' ', end='')
    print('*', end='')
    for _ in range(1, row):
        print(' *', end='')
    print()

#   lower part

for row in reversed(range(1, n)):
    for _ in range(1, n - row):
        print(' ', end='')
    print(' *', end='')
    for _ in range(1, row):
        print(' *', end='')
    print()
