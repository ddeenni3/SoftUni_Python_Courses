rent = int(input())

statues = rent * 0.7
catering = statues * 0.85
sound_equipment = catering * 0.5

total_cost = rent + sound_equipment + statues + catering

print(f'{total_cost:.2f}')

