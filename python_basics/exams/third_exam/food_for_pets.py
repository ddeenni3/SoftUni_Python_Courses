days = int(input())
total_food = float(input())
dog = 0
cat = 0
biscuit = 0
total = 0

for day in range(1, days + 1):
    current_dog = int(input())
    current_cat = int(input())
    dog += current_dog
    cat += current_cat
    total += dog + cat
    if day % 3 == 0:
        biscuit += (current_dog + current_cat) * 0.1

print(f'Total eaten biscuits: {round(biscuit)}gr.')
print(f'{(dog + cat) / total_food * 100:.2f}% of the food has been eaten.')
print(f"{dog / (dog + cat) * 100:.2f}% eaten from the dog.")
print(f'{cat / (dog + cat) * 100:.2f}% eaten from the cat.')


