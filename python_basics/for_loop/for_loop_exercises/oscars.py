actor_name = input()
academy_points = float(input())
jury = int(input())

needed_points = 1250.5


for i in range(jury):
    judge = input()
    score = float(input())
    academy_points += len(judge) * score / 2
    if academy_points > needed_points:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!')
        break

if academy_points <= needed_points:
    print(f'Sorry, {actor_name} you need {abs(academy_points - needed_points):.1f} more!')

