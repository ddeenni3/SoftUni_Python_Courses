def valid_index(index: int, some_list: list):
    if 0 <= index < len(some_list):
        if not some_list[index] == -1:
            return True


targets = [int(x) for x in input().split()]

shot_targets = 0

while True:
    command = input()
    if command == 'End':
        print(f'Shot targets: {shot_targets} -> {" ".join(str(x) for x in targets)}')
        break
    current_index = int(command)
    if valid_index(current_index, targets):
        shot_target = targets[current_index]
        targets[current_index] = -1
        shot_targets += 1
        for target_index in range(len(targets)):
            if targets[target_index] > shot_target and not targets[target_index] == -1:
                targets[target_index] -= shot_target
            elif targets[target_index] <= shot_target and not targets[target_index] == -1:
                targets[target_index] += shot_target
