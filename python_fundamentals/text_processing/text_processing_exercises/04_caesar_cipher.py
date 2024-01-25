text_to_cypher = input()
cyphered_text = ''
for symbol in text_to_cypher:
    cyphered_text += chr(ord(symbol) + 3)
print(cyphered_text)
