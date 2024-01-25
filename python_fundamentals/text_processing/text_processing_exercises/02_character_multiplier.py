first_string, second_string = input().split()

longer_string = []
shorter_string = []

if len(first_string) > len(second_string):
    longer_string = first_string
    shorter_string = second_string
elif len(second_string) > len(first_string):
    longer_string = second_string
    shorter_string = first_string
else:
    longer_string = first_string
    shorter_string = second_string


total = 0

for index in range(len(shorter_string)):
    total += ord(first_string[index]) * ord(second_string[index])

for index in range(len(shorter_string), len(longer_string)):
    total += ord(longer_string[index])

print(total)