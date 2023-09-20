actor_name = input()
starting_points = float(input())
n = int(input())

points_needed = 1250.5

for actor in range(n):
    judge_name = input()
    score = float(input())
    total_score = (len(judge_name) * score) / 2
    starting_points += total_score
    if starting_points >= points_needed:
        break

if starting_points > points_needed:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {starting_points:.1f}!')
else:
    print(f'Sorry, {actor_name} you need {abs(starting_points - points_needed):.1f} more!')

