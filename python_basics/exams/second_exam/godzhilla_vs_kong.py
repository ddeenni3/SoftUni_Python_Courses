budget = float(input())
statists = int(input())
price_per_statist = float(input())

decorations = budget * 0.1

if statists > 150:
    price_per_statist *= 0.9

total = statists * price_per_statist + decorations
diff = abs(total - budget)

if budget >= total:
    print(f'Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
else:
    print(f'Not enough money!')
    print(f"Wingard needs {diff:.2f} leva more.")
