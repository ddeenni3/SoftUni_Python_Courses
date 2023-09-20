movie = input()


student = 0
standard = 0
kid = 0

break_flag = False


while movie != 'Finish':
    free_seats = int(input())
    total_seats = free_seats
    current_movie = 0
    while free_seats > 0:
        ticket_type = input()
        if ticket_type == 'End':
            break_flag = True
            break
        if ticket_type == 'student':
            student += 1
            current_movie += 1
            free_seats -= 1
        elif ticket_type == 'standard':
            standard += 1
            current_movie += 1
            free_seats -= 1
        elif ticket_type == 'kid':
            kid += 1
            current_movie += 1
            free_seats -= 1
    print(f'{movie} - {current_movie / total_seats * 100:.2f}% full.')
    movie = input()

total = student + standard + kid

print(f'Total tickets: {total}')
print(f'{student / total * 100:.2f}% student tickets.')
print(f'{standard / total * 100:.2f}% standard tickets.')
print(f'{kid / total * 100:.2f}% kids tickets.')
