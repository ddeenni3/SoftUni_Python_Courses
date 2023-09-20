from math import *
crew_amount = int(input())
entry_cost = float(input())
chair_price = float(input())
umbrella_price = float(input())

total_entry = crew_amount * entry_cost

umbrella_crew = ceil(crew_amount / 2)
chair_crew = ceil(crew_amount * 0.75)

total_chair = chair_crew * chair_price
total_umbrella = umbrella_crew * umbrella_price

total_cost = total_chair + total_entry + total_umbrella

print(f'{total_cost:.2f} lv.')
