projection_type = input()
rows = int(input())
lines = int(input())

ticket_price = 0

full_house = rows * lines

if projection_type == 'Premiere':
    ticket_price = 12
elif projection_type == 'Normal':
    ticket_price = 7.5
elif projection_type == 'Discount':
    ticket_price = 5

total_sum = full_house * ticket_price

print(f'{total_sum:.2f} leva')
