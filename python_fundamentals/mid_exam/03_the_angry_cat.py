price_ratings = [int(x) for x in input().split(', ')]
starting_index = int(input())
items_to_break = input()

price_starting_index = price_ratings[starting_index]
items_to_the_left = price_ratings[:starting_index]
items_to_the_right = price_ratings[starting_index + 1:]
items_to_break_left = []
items_to_break_right = []

if items_to_break == 'cheap':
    items_to_break_left = [x for x in items_to_the_left if x < price_starting_index]
    items_to_break_right = [x for x in items_to_the_right if x < price_starting_index]
elif items_to_break == 'expensive':
    items_to_break_left = [x for x in items_to_the_left if x >= price_starting_index]
    items_to_break_right = [x for x in items_to_the_right if x >= price_starting_index]

if sum(items_to_break_left) >= sum(items_to_break_right):
    print(f"Left - {sum(items_to_break_left)}")
else:
    print(f'Right - {sum(items_to_break_right)}')
