capacity = int(input())

total_money = 0

while True:
    command = input()
    if command == 'Movie time!':
        print(f'There are {capacity} seats left in the cinema.')
        break
    viewers = int(command)
    capacity -= viewers
    if capacity < 0:
        print(f'The cinema is full.')
        break
    total_money += viewers * 5
    if viewers % 3 == 0:
        total_money -= 5
print(f'Cinema income - {total_money} lv.')
