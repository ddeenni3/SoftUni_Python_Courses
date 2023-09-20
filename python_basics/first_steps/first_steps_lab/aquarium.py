length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
others = float(input())
others /= 100

volume_aquarium = length_cm * width_cm * height_cm
volume_aquarium_litres = volume_aquarium / 1000
needed_litres = volume_aquarium_litres * (1-others)

print(needed_litres)
