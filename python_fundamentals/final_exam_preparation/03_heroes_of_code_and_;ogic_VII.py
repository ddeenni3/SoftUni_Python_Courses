number_of_heroes = int(input())

heroes = {}

for _ in range(number_of_heroes):
    name, hit_points, mana = input().split()
    heroes[name] = {'hp': int(hit_points), 'mana': int(mana)}

while True:
    command = input().split(' - ')
    if command[0] == 'End':
        break
    elif command[0] == 'CastSpell':
        hero_name, mana_needed, spell_name = command[1], int(command[2]), command[3]
        if heroes[hero_name]['mana'] >= mana_needed:
            heroes[hero_name]['mana'] -= mana_needed
            print(f'{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]["mana"]} MP!')
        else:
            print(f'{hero_name} does not have enough MP to cast {spell_name}!')
    elif command[0] == 'TakeDamage':
        hero_name, damage, attacker = command[1], int(command[2]), command[3]
        heroes[hero_name]['hp'] -= damage
        if heroes[hero_name]['hp'] > 0:
            print(f'{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]["hp"]} HP left!')
        else:
            del heroes[hero_name]
            print(f'{hero_name} has been killed by {attacker}!')
    elif command[0] == 'Recharge':
        hero_name, amount = command[1], int(command[2])
        increase_amount = min(200 - heroes[hero_name]['mana'], amount)
        heroes[hero_name]['mana'] += increase_amount
        print(f'{hero_name} recharged for {increase_amount} MP!')
    elif command[0] == 'Heal':
        hero_name, amount = command[1], int(command[2])
        increase_amount = min(100 - heroes[hero_name]['hp'], amount)
        heroes[hero_name]['hp'] += increase_amount
        print(f'{hero_name} healed for {increase_amount} HP!')

if heroes:
    for hero in heroes:
        print(f'''{hero}
  HP: {heroes[hero]["hp"]}
  MP: {heroes[hero]["mana"]}''')
