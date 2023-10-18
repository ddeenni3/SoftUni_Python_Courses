people_waiting = int(input())
lift_state = [int(x) for x in input().split()]
is_full = False

while people_waiting > 0:
    for cabin in range(len(lift_state)):
        while lift_state[cabin] < 4:
            if people_waiting == 0:
                break
            lift_state[cabin] += 1
            people_waiting -= 1
            if len(lift_state) * 4 == sum(lift_state):
                is_full = True
                break
        if is_full:
            break
    if is_full:
        break


total_spots = len(lift_state) * 4
total_occupied = sum(lift_state)
total_free = total_spots - total_occupied

if total_free > 0:
    print(f'The lift has empty spots!\n'
          f'{" ".join(str(x) for x in lift_state)}')
elif people_waiting > 0:
    print(f'There isn\'t enough space! {people_waiting} people in a queue!\n'
          f'{" ".join(str(x) for x in lift_state)}')
else:
    print(f'{" ".join(str(x) for x in lift_state)}')
