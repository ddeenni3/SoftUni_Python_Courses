from collections import deque

kids = deque(input().split())

hot_count = int(input())

hot_count -= 1

while len(kids) > 1:
    kids.rotate(-hot_count)

    print(f'Removed {kids.popleft()}')

print(f'Last is {kids.pop()}')
