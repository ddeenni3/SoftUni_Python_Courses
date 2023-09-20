budget = float(input())
nights = int(input())
price_per_night = float(input())
percentage_extra_cost = int(input())

if nights > 7:
    price_per_night *= 0.95

total_cost = nights * price_per_night + ((percentage_extra_cost / 100) * budget)

diff = abs(total_cost - budget)

if total_cost > budget:
    print(f"{diff:.2f} leva needed.")
else:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
