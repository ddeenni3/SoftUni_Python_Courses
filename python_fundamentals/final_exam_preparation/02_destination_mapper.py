import re

places = input()

pattern = r'([=/])([A-Z][A-Za-z]{2,})(\1)'

matches = re.findall(pattern, places)

destinations = []
travel_points = 0

for match in matches:
    destinations.append(match[1])
    travel_points += len(match[1])

print(f'Destinations: {", ".join(destinations)}')
print(f'Travel Points: {travel_points}')
