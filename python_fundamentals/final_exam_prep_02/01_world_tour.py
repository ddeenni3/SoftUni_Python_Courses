stops = input()

while True:
    command = input().split()
    if command[0] == 'Travel':
        break
    elif command[0] == 'Add':
        actions = command[1].split(':')
        index = int(actions[1])
        string = actions[2]
        if index < len(stops):
            stops = stops[:index] + string + stops[index:]
    elif command[0] == 'Remove':
        actions = command[1].split(':')
        start_index = int(actions[1])
        end_index = int(actions[2])
        if start_index < len(stops) and end_index < len(stops):
            stops = stops[:start_index] + stops[end_index + 1:]
    else:
        actions = command[0].split(':')
        old_string = actions[1]
        new_string = actions[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
    print(stops)
print(f'Ready for world tour! Planned stops: {stops}')
