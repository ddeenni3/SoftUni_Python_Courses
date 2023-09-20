chicken_menu_price = 10.35
fish_menu_price = 12.40
vegan_menu_price = 8.15
delivery_cost = 2.50

amount_chicken = int(input())
amount_fish = int(input())
amount_vegan = int(input())

sum_menus = (amount_fish * fish_menu_price) + (amount_vegan * vegan_menu_price) + (amount_chicken * chicken_menu_price)
dessert = 0.2 * sum_menus

total_cost = sum_menus + dessert + delivery_cost

print(total_cost)

