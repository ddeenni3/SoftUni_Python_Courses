import sys

string = input().split(' ')
n = int(input())

integers = list(map(int, string))

smallest_element = sys.maxsize

for _ in range(n):
    smallest_element = sys.maxsize
    for element in integers:
        if element < smallest_element:
            smallest_element = element
    integers.remove(smallest_element)

print(', '.join(map(str, integers)))
