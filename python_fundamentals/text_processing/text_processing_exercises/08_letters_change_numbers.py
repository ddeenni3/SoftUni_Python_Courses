text = [x.strip() for x in input().split()]

total = 0
current_total = 0
first_letters = []
second_letters = []
current_num = ''

for current_word in text:
    for symbol in current_word:
        if symbol.isalpha():
            if current_num:
                second_letters.append(symbol)
            else:
                first_letters.append(symbol)
        else:
            current_num += symbol
    current_total += int(current_num)
    current_num = ''
    for letter in first_letters:
        if letter.isupper():
            number = ord(letter) - 64
            current_total /= number
        else:
            number = ord(letter) - 96
            current_total *= number
    for letter in second_letters:
        if letter.isupper():
            number = ord(letter) - 64
            current_total -= number
        else:
            number = ord(letter) - 96
            current_total += number
    total += current_total
    first_letters = []
    second_letters = []
    current_total = 0

print(f"{total:.2f}")


