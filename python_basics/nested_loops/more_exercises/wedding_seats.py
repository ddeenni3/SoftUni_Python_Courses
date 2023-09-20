interval_end = (input())
rows = int(input())
seats_odd_row = int(input())

total_seats = 0

for char in range(ord('A'), ord(interval_end) + 1):
    for row in range(1, rows + 1):
        if row % 2 == 0:
            for seat in range(97, (seats_odd_row + 96 + 2) + 1):
                total_seats += 1
                print(f'{chr(char)}{row}{chr(seat)}')
        else:
            for seats in range(97, (seats_odd_row + 96) + 1):
                total_seats += 1
                print(f'{chr(char)}{row}{chr(seats)}')
    rows += 1
print(total_seats)
