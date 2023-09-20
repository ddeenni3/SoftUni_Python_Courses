tournaments = int(input())
rank_points = int(input())

points = 0
tournaments_won = 0

for i in range(tournaments):
    stage = input()
    if stage == 'W':
        points += 2000
        tournaments_won += 1
    elif stage == 'F':
        points += 1200
    elif stage == 'SF':
        points += 720

final_points = points + rank_points
average_points = points // tournaments
percentage_tourney_won = tournaments_won / tournaments * 100

print(f'Final points: {final_points}')
print(f'Average points: {average_points}')
print(f'{percentage_tourney_won:.2f}%')
