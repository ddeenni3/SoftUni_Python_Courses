floors = int(input())
rooms = int(input())

for floor in reversed(range(1, floors + 1)):
    for room in range(rooms):
        if floor == floors:
            room_type = 'L'
        else:
            room_type = 'A' if floor % 2 else 'O'
        print(f"{room_type}{floor}{room}", end=' ')
    print()
