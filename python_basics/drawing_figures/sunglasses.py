n = int(input())

stars = '*'
spaces = ' '
dash = '/'
line = '|'

print(f'{2 * n * stars}{spaces * n}{2 * n * stars}')

for i in range(n - 2):
    if i == (n - 1) // 2 - 1:
        print(f'{stars}{(2 * n - 2) * dash}{stars}{n * line}{stars}{(2 * n - 2) * dash}{stars}')
    else:
        print(f'{stars}{(2 * n - 2) * dash}{stars}{n * spaces}{stars}{(2 * n - 2) * dash}{stars}')
print(f'{2 * n * stars}{spaces * n}{2 * n * stars}')
# if i == (n - 1) // 2 - 1:
#     print(f'{stars}{2 * n * dash}{stars}{n * line}{stars}{2 * n * dash}{stars}')


