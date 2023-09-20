# Read user input
n = int(input())

# Logic


min_value = 0
max_value = 0

for i in range(n):
    num = int(input())
    if i == 0:
        min_value = num
        max_value = num

    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num

# Print output

print(f'Max number: {max_value}')
print(f'Min number: {min_value}')
