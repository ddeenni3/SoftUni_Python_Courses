numbers_list = input().split()
remove_count = int(input())

numbers_to_int = []

for num in numbers_list:
    numbers_to_int.append(int(num))


for _ in range(remove_count):
    smallest_num = numbers_to_int[0]
    for num in numbers_to_int:
        if num < smallest_num:
            smallest_num = num
    numbers_to_int.remove(smallest_num)


print(', '.join(map(str, numbers_to_int)))





