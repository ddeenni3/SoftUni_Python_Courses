def to_do_list():

    list_of_commands = []

    while True:
        command = input()
        if command == 'End':
            break
        list_of_commands.append(command)
        sorted_commands = sorted(list_of_commands, key=lambda x: int(x.split('-')[0]))

    return sorted_commands


sorted_notes = to_do_list()

print([note.split('-')[1] for note in sorted_notes])
