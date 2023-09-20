command = input()

student = 0
standard = 0
kid = 0


while command != 'Finish':
    empty_seats = int(input())
    total_movie = 0
    while empty_seats > 0:
        ticket_type = input()
        if ticket_type == 'End':
            break
        if ticket_type == 'student':
            empty_seats -= 1
            total_movie += 1
            student += 1
        elif ticket_type == 'standard':
            empty_seats -= 1
            total_movie += 1
            standard += 1
        elif ticket_type == 'kid':
            empty_seats -= 1
            total_movie += 1
            kid += 1

    print(f'{command} - {total_movie / (empty_seats + total_movie) * 100:.2f}% full.')
    command = input()

total_tickets = student + standard + kid

print(f'Total tickets: {total_tickets}')
print(f'{student / total_tickets * 100:.2f}% student tickets.')
print(f'{standard / total_tickets * 100:.2f}% standard tickets.')
print(f'{kid / total_tickets * 100:.2f}% kids tickets.')
