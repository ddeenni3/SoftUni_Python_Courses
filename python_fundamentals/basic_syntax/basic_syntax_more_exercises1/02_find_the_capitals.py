string = input()
capitals = []

for ch in range(len(string)):
    if string[ch].isupper():
        capitals.append(ch)

print(capitals)