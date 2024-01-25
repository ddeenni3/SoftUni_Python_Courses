string = input()

numbers = ''
letters = ''
symbols = ''


for char in string:
    if char.isdigit():
        numbers += char
    elif char.isalpha():
        letters += char
    elif not char.isalnum():
        symbols += char

print(numbers)
print(letters)
print(symbols)
