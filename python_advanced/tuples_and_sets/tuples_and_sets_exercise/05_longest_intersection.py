longest_intersection = []

for _ in range(int(input())):
    intersections = input().split('-')
    first_start, first_end = intersections[0].split(',')
    second_start, second_end = intersections[1].split(',')
    first_intersection = set(range(int(first_start), int(first_end) + 1))
    second_intersection = set(range(int(second_start), int(second_end) + 1))
    intersection = first_intersection.intersection(second_intersection)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f'Longest intersection is [{", ".join(str(x) for x in longest_intersection)}] '
      f'with length {len(longest_intersection)}')


