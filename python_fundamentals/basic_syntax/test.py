# num = int(input())
# counter = 1
#
# for i in range(1, num+1):
#     for j in range(1, counter + 1):
#         if counter % 2 != 0:
#             print("*", end='')
#     counter += 2
#     print()


# rows = int(input())
#
# for i in range(rows):
#     for j in range(rows):
#         print('$', end=' ')
#     print()


# rows = int(input())
#
# for row in range(rows):
#     for column in range(row, rows):
#         print('*', end=' ')
#     print()


# n = int(input())
#
# for i in range(n):
#     for j in range(i, n):
#         print(' ', end=' ')
#     for j in range(i + 1):
#         print('*', end=' ')
#     print()


# n = 5
# for i in range(n):
#     for j in range(i + 1):
#         print('*', end=' ')
#     print()
#
#
# n = 5
# for i in range(n):
#     for j in range(i, n):
#         print('*', end=' ')
#     print()
#
# n = 5
# for i in range(n):
#     for j in range(i, n):
#         print(' ', end=' ')
#     for j in range(i + 1):
#         print('*', end=' ')
#     print()

# n = 5
# for i in range(n):
#     for j in range(i, n):
#         print(' ', end=' ')
#     for j in range(i + 1):
#         print('*', end=' ')
#     for j in range(i):
#         print('*', end=' ')
#     print()

# n = 5
# for rows in range(n):
#     for column in range(rows + 1):
#         print(' ', end=' ')
#     for column in range(rows, n):
#         print('*', end=' ')
#     for column in range(rows, n - 1):
#         print('*', end=' ')
#     print()

# n = 5
# for rows in range(n):
#     for column in range(rows, n):
#         print(' ', end='')
#     for column in range(rows + 1):
#         print('*', end=' ')
#     print()

n = 5
for row in range(n - 1):
    for column in range(row + 1):
        print('*', end=' ')
    for column in range(row + 1, n):
        print(' ', end=' ')
    for column in range(row + 1, n):
        print(' ', end=' ')
    for column in range(row + 1):
        print('*', end=' ')
    print()
for row in range(n):
    for column in range(row, n):
        print('*', end=' ')
    for column in range(row):
        print(' ', end=' ')
    for column in range(row):
        print(' ', end=' ')
    for column in range(row, n):
        print('*', end=' ')
    print()
# for row in range(n):
#     for column in range(row, n - 1):
#         print('*', end=' ')
#     for column in range(row + 1):
#         print(' ', end=' ')
#     print()
#
#
# for row in range(n):
#     for column in range(row, n + 1):
#         print(' ', end=' ')
#     for column in range(row):
#         print('*', end=' ')
#     print()
# for row in range(n):
#     for column in range(row + 1):
#         print(' ', end=' ')
#     for column in range(row, n):
#         print('*', end=' ')
#     print()


# n = 5
# for rows in range(n):
#     # for column in range(rows + 1):
#     #     print('$', end='')
#     for column in range(rows, n):
#         print('$', end=' ')
#     print()


# n = 4
# for row in range(n):
#     for column in range(row + 1):
#         print('*', end=' ')
#     print()
# for rows in range(n):
#     for column in range(rows + 1):
#         print('$', end='')
#     for column in range(rows, n):
#         print('$', end=' ')
#     print()