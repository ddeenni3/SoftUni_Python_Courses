number_of_letters = int(input())

total = 0

for ch in range(number_of_letters):
    letter = input()
    total += ord(letter)

print(f'The sum equals: {total}')
