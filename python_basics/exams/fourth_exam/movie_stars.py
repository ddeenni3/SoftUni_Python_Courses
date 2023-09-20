budget = float(input())

while True:
    command = input()
    if command == 'ACTION':
        print(f'We are left with {budget:.2f} leva.')
        break
    actor_name = command
    if len(actor_name) <= 15:
        pay = float(input())
        budget -= pay
    else:
        pay = budget * 0.2
        budget -= pay
    if budget < 0:
        print(f'We need {abs(budget):.2f} leva for our actors.')
        break
