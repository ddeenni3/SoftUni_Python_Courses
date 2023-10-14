def check_empty_seats(rooms: int):
    total_chairs = 0
    total_visitors = 0
    for room in range(1, number_of_rooms + 1):
        room_info = input().split()
        empty_seats = list(room_info[0]).count('X')
        visitors = int(room_info[-1])
        total_chairs += empty_seats
        total_visitors += visitors
        if empty_seats < visitors:
            needed_chairs_in_room = visitors - empty_seats
            print(f'{needed_chairs_in_room} more chairs needed in room {room}')
    return total_chairs - total_visitors


number_of_rooms = int(input())
total_free_chairs = check_empty_seats(number_of_rooms)
if total_free_chairs >= 0:
    print(f'Game On, {total_free_chairs} free chairs left')
