n = int(input())
command = input()

combined = []

for _ in range(n):
    string = input()
    combined.append(string)

print(combined)

filtered = []

for element in combined:
    if command in element:
        filtered.append(element)

print(filtered)
