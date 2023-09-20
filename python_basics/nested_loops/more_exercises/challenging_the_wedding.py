male_clients = int(input())
female_clients = int(input())
total_tables = int(input())

total_couples = male_clients * female_clients

empty_seats = True

for male in range(1, male_clients + 1):
    for female in range(1, female_clients + 1):
        print(f'({male} <-> {female})', end=' ')
        total_tables -= 1
        total_couples -= 1
        if total_tables <= 0 or total_couples <= 0:
            empty_seats = False
            break
    if not empty_seats:
        break
