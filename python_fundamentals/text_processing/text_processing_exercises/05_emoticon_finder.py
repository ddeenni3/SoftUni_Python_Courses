text = input().split()

for element in text:
    element = list(element)
    for pos, symbol in enumerate(element):
        if symbol == ':':
            print(symbol + element[pos + 1])
