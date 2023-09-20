daily_goal = 10000
steps_counter = 0


while True:
    command = input()
    if command == 'Going home':
        steps_to_home = int(input())
        steps_counter += steps_to_home
        break
    steps_counter += int(command)
    if steps_counter >= daily_goal:
        break

diff = abs(steps_counter - daily_goal)

if steps_counter >= daily_goal:
    print('Goal reached! Good job!')
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
