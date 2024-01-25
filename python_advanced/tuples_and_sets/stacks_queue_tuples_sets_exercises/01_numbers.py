first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

for _ in range(int(input())):
    command, sequence, *data = input().split()
    current_command = command + ' ' + sequence
    if current_command == 'Add First':
        [first_sequence.add(int(x)) for x in data]
    elif current_command == 'Add Second':
        [second_sequence.add(int(x)) for x in data]
    elif current_command == 'Remove First':
        [first_sequence.discard(int(x)) for x in data]
    elif current_command == 'Remove Second':
        [second_sequence.discard(int(x)) for x in data]
    elif current_command == 'Check Subset':
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')
