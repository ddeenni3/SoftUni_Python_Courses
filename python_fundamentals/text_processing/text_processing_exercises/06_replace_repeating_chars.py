input_string = input()

unique_symbols = ''
last_symbol = ''

for symbol in input_string:
    if last_symbol != symbol:
        last_symbol = symbol
        unique_symbols += last_symbol

print(unique_symbols)
