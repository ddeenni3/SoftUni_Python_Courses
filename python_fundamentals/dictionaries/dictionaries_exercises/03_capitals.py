counties = input().split(', ')
capitals = input().split(', ')

final_output = {counties[index]: capitals[index] for index in range(len(capitals))}

for country, capital in final_output.items():
    print(f'{country} -> {capital}')