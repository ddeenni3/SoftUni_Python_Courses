animal = input()

animal_type = 'unknown'

if animal == 'dog':
    animal_type = 'mammal'
elif animal in ['crocodile', 'tortoise', 'snake']:
    animal_type = 'reptile'

print(animal_type)
