from collections import deque

station_info = deque([[int(x) for x in input().split()]for _ in range(int(input()))])

station_info_copy = station_info.copy()

index = 0
fuel = 0

while station_info_copy:
    gas, distance = station_info_copy.popleft()
    fuel += gas

    if fuel >= distance:
        fuel -= distance
    else:
        station_info.rotate(-1)
        station_info_copy = station_info.copy()
        index += 1
        fuel = 0

print(index)
