odd_set = set()
even_set = set()

for i in range(1, int(input()) + 1):
    name = input()
    name_score = 0
    for char in name:
        name_score += ord(char)
    name_score //= i
    if name_score % 2 == 0:
        even_set.add(name_score)
    else:
        odd_set.add(name_score)

if sum(even_set) > sum(odd_set):
    print(*(odd_set.symmetric_difference(even_set)), sep=', ')
elif sum(even_set) == sum(odd_set):
    print(*(odd_set.union(even_set)), sep=', ')
else:
    print(*(odd_set.difference(even_set)), sep=', ')