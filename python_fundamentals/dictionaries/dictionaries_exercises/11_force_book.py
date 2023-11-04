force_users = {}

while True:
    command = input()
    if command == 'Lumpawaroo':
        break
    elif '|' in command:
        force_side, force_user = command.split(' | ')
        user_existing = False
        for value in force_users.values():
            if force_user in value:
                user_existing = True
                break
        if not user_existing:
            if force_side not in force_users.keys():
                force_users[force_side] = []
            force_users[force_side].append(force_user)
    elif '->' in command:
        force_user, force_side = command.split(' -> ')
        for value in force_users.values():
            if force_user in value:
                value.remove(force_user)
                break
        if force_side not in force_users.keys():
            force_users[force_side] = []
        force_users[force_side].append(force_user)
        print(f'{force_user} joins the {force_side} side!')

for side, users in force_users.items():
    if len(users) > 0:
        print(f'Side: {side}, Members: {len(users)}')
        for user in users:
            print(f'! {user}')
