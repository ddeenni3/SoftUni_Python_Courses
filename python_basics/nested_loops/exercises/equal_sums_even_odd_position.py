starting_interval = int(input())
ending_interval = int(input())

for i in range(starting_interval, ending_interval + 1):
    current_num = str(i)
    odd_sum = 0
    even_sum = 0
    for index in range(len(current_num)):

        if index % 2 == 0:
            odd_sum += int(current_num[index])
        else:
            even_sum += int(current_num[index])

    if odd_sum == even_sum:
        print(current_num, end=' ')
