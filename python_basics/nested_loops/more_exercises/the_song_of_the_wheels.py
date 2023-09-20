control_number = int(input())
password_counter = 0
print_password = None

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if control_number == (a * b) + (c * d) and a < b and c > d:
                    print(f'{a}{b}{c}{d}', end=' ')
                    password_counter += 1
                    if password_counter == 4:
                        print_password = f'{a}{b}{c}{d}'

if password_counter < 4:
    print()
    print('No!')
else:
    print()
    print(f'Password: {print_password}')


