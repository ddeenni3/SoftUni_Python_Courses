football_club = input()
games_amount = int(input())

w = 0
d = 0
ls = 0
total_points = 0


if games_amount <= 0:
    print(f"{football_club} hasn't played any games during this season.")
else:
    for game in range(games_amount):
        result = input()
        if result == 'W':
            w += 1
            total_points += 3
        elif result == 'D':
            d += 1
            total_points += 1
        elif result == 'L':
            ls += 1

    print(f"{football_club} has won {total_points} points during this season.")
    print(f'Total stats:')
    print(f'## W: {w}')
    print(f'## D: {d}')
    print(f'## L: {ls}')
    print(f'Win rate: {w / games_amount * 100:.2f}%')

