# n = 5
#
# for row in range(n - 1):
#     # for column in range(row + 1):
#     #     print('*', end=' ')
#     # for column in range(row + 1, n):
#     #     print(' ', end=' ')
#     # for column in range(row + 1, n):
#     #     print(' ', end=' ')
#     # for column in range(row + 1):
#     #     print('*', end=' ')
#     print('* ' * (row + 1), end='')
#     print((n - 2) * ' $ ', end='')
#     print('*' * (row + 1))
#     print()
# for row in range(n):
#     for column in range(row, n):
#         print('*', end=' ')
#     for column in range(row):
#         print(' ', end=' ')
#     for column in range(row):
#         print(' ', end=' ')
#     for column in range(row, n):
#         print('*', end=' ')
#     print()


name = 'Denkata_E_Dibel'


def greet_user():
    print(f'Hi, {name}!')


if name == "Denkata_E_Dibel":
    greet_user()
