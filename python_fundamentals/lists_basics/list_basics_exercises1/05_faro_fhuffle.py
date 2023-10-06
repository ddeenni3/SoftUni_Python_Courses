cards = input().split()
shuffles_count = int(input())

for shuffle in range(shuffles_count):
    middle = len(cards) // 2
    left_part = cards[:middle]
    right_part = cards[middle:]
    shuffled = []
    for element in range(len(left_part)):
        shuffled.append(left_part[element])
        shuffled.append(right_part[element])
    cards = shuffled

print(shuffled)
