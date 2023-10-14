pokemon_distances = [int(x) for x in input().split(' ')]

removed_elements = []

while pokemon_distances:
    pokemon_index = int(input())
    if pokemon_index < 0:
        removed_elements.append(pokemon_distances[0])
        pokemon_distances[0] = pokemon_distances[-1]
    elif pokemon_index > len(pokemon_distances) - 1:
        removed_elements.append(pokemon_distances[-1])
        pokemon_distances[-1] = pokemon_distances[0]
    else:
        removed_elements.append(pokemon_distances.pop(pokemon_index))
    pokemon_distances = [x + removed_elements[- 1] if x <= removed_elements[- 1] else x - removed_elements[- 1]
                         for x in pokemon_distances]

print(sum(removed_elements))
