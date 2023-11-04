materials = {'shards': 0, 'fragments': 0, 'motes': 0}
gathered_materials = False

while True:
    command = [x for x in input().split()]
    for index in range(0, len(command), 2):
        material = command[index + 1]. lower()
        quantity = int(command[index])
        if material not in materials.keys():
            materials[material] = int(quantity)
        else:
            materials[material] += int(quantity)
        legendary_item = ''
        if materials['shards'] >= 250:
            gathered_materials = True
            legendary_item = 'Shadowmourne'
            materials['shards'] -= 250
        elif materials['fragments'] >= 250:
            gathered_materials = True
            legendary_item = 'Valanyr'
            materials['fragments'] -= 250
        elif materials['motes'] >= 250:
            gathered_materials = True
            legendary_item = 'Dragonwrath'
            materials['motes'] -= 250
        if gathered_materials:
            print(f'{legendary_item} obtained!')
            for material, quantity in materials.items():
                print(f'{material}: {quantity}')
            break
    if gathered_materials:
        break
