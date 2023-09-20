mousala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

climber_groups = int(input())

for climbers in range(climber_groups):
    climber_amount = int(input())
    if climber_amount <= 5:
        mousala += climber_amount
    elif climber_amount <= 12:
        montblanc += climber_amount
    elif climber_amount <= 25:
        kilimanjaro += climber_amount
    elif climber_amount <= 40:
        k2 += climber_amount
    else:
        everest += climber_amount

total = montblanc + mousala + k2 + kilimanjaro + everest

print(f'{mousala / total * 100:.2f}%')
print(f'{montblanc / total * 100:.2f}%')
print(f'{kilimanjaro / total * 100:.2f}%')
print(f'{k2 / total * 100:.2f}%')
print(f'{everest / total * 100:.2f}%')
