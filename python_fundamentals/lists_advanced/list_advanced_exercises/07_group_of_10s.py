numbers = list(map(int, input().split(', ')))

previous_boundary = 0
boundary = 10

while numbers:
    current_list = []
    for number in range(len(numbers) - 1, - 1, - 1):
        if previous_boundary < numbers[number] <= boundary:
            current_list.append(numbers[number])
            numbers.remove(numbers[number])
    print(f'Group of {boundary}\'s: {current_list[::-1]}')
    boundary += 10
    previous_boundary += 10
