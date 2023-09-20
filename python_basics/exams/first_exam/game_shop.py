n = int(input())
hs = 0
fortnite = 0
ow = 0
others = 0


for game in range(n):
    game_name = input()
    if game_name == 'Hearthstone':
        hs += 1
    elif game_name == 'Fornite':
        fortnite += 1
    elif game_name == 'Overwatch':
        ow += 1
    else:
        others += 1

total = hs + fortnite + ow + others

print(f'Hearthstone - {hs / total * 100:.2f}%')
print(f'Fornite - {fortnite / total * 100:.2f}%')
print(f'Overwatch - {ow / total * 100:.2f}%')
print(f'Others - {others / total * 100:.2f}%')


