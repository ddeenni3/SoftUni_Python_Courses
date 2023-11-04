food_quantities = input().split()

inventory = {}

for i in range(0, len(food_quantities), 2):
    food = food_quantities[i]
    quantity = int(food_quantities[i + 1])
    inventory[food] = quantity

print(inventory)
