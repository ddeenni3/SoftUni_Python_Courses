from math import *

wall_height = int(input())
wall_width = int(input())
percent = int(input())

total_surface = wall_width * wall_height * 4

percent = 1 - percent / 100

total_surface *= percent

total_surface = ceil(total_surface)

command = input()
while command != 'Tired!':
    total_surface -= int(command)
    if total_surface <= 0:
        break
    command = input()

if total_surface > 0:
    print(f'{abs(total_surface)} quadratic m left.')
elif total_surface < 0:
    print(f'All walls are painted and you have {abs(total_surface)} l paint left!')
else:
    print(f'All walls are painted! Great job, Pesho!')
