bottles_soap = int(input())

total_soap = bottles_soap * 750

counter = 0

plates = 0
pots = 0

while total_soap >= 0:
    counter += 1
    command = input()
    if command == 'End':
        break
    command = int(command)
    if counter == 3:
        pots += command
        total_soap -= command * 15
        counter = 0
    else:
        plates += command
        total_soap -= command * 5

if total_soap >= 0:
    print(f'Detergent was enough!')
    print(f"{plates} dishes and {pots} pots were washed.")
    print(f'Leftover detergent {total_soap} ml.')
else:
    print(f'Not enough detergent, {abs(total_soap)} ml. more necessary!')
