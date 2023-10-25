class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fish.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ''
        if species == 'mammal':
            result = f'Mammals in {self.name}: {", ".join(self.mammals)}'
        elif species == 'fish':
            result = f'Fishes in {self.name}: {", ".join(self.fish)}'
        elif species == 'bird':
            result = f'Birds in {self.name}: {", ".join(self.birds)}'

        result += f'\nTotal animals: {Zoo.__animals}'

        return result


zoo_name = input()
current_zoo = Zoo(zoo_name)
animals = int(input())

for animal in range(animals):
    species, name = input().split()
    current_zoo.add_animal(species, name)

species_info = input()
print(current_zoo.get_info(species_info))

