first_set_len, second_set_len = input().split()

first_set = set([int(input()) for _ in range(int(first_set_len))])
second_set = set([int(input()) for _ in range(int(second_set_len))])

print(*(first_set.intersection(second_set)), sep='\n')