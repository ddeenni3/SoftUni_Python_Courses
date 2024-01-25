symbol_occurrences = {}

for char in input():
    symbol_occurrences[char] = symbol_occurrences.get(char, 0) + 1

for key, occurrence in sorted(symbol_occurrences.items()):
    print(f'{key}: {occurrence} time/s')
