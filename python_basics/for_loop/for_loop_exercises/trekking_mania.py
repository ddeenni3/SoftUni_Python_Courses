groups = int(input())

musala = 0
monblanc = 0
kilimandjaro = 0
k2 = 0
everest = 0

total = 0

for i in range(groups):
    climbers = int(input())
    total += climbers
    if climbers <= 5:
        musala += climbers
    elif climbers <= 12:
        monblanc += climbers
    elif climbers <= 25:
        kilimandjaro += climbers
    elif climbers <= 40:
        k2 += climbers
    else:
        everest += climbers

print(f'{musala / total * 100:.2f}%')
print(f'{monblanc / total * 100:.2f}%')
print(f'{kilimandjaro / total * 100:.2f}%')
print(f'{k2 / total * 100:.2f}%')
print(f'{everest / total * 100:.2f}%')
