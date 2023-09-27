n = int(input())

positives = []
negatives = []


for _ in range(n):
    number = int(input())

    if number >= 0:
        positives.append(number)
    else:
        negatives.append(number)

print(positives)
print(negatives)
print('Count of positives:', len(positives))
print('Sum of negatives:', sum(negatives))
