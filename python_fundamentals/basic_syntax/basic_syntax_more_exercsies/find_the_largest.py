number = input()

l1 = list(number)
l1.sort(reverse=True)
max_num = ''.join(l1)

print(max_num)
