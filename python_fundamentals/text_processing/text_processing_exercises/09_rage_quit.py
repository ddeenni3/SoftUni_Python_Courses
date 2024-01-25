text = input()

symbols = []
elements = []
digits = []

current_number = ''
current_element = ''

for index in range(len(text)):
    if not text[index].isnumeric():
        symbol = text[index].upper()
        current_element += symbol
        symbols.append(symbol)
    else:
        for next_index in range(index, len(text)):
            if not text[next_index].isnumeric():
                break
            else:
                current_number += text[next_index]
        digits.append(int(current_number))
        elements.append(current_element)
        current_number = ''
        current_element = ''
unique_elements = len(set(symbols))
print(f'Unique symbols used: {unique_elements}')
for index in range(len(digits)):
    print(f'{digits[index] * elements[index]}', end='')
