food_inventory = input().split()
items_to_search = input().split()

inventory = {}

for i in range(0, len(food_inventory), 2):
    food = food_inventory[i]
    quantity = int(food_inventory[i + 1])
    inventory[food] = quantity

for item in items_to_search:
    if item in inventory.keys():
        print(f'We have {inventory[item]} of {item} left')
    else:
        print(f'Sorry, we don\'t have {item}')
