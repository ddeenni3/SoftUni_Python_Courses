string = input()

herd = string.split()

herd.reverse()

for i in range(len(herd)):
    if herd[i] == 'wolf,' or herd[i] == 'wolf':
        if i == 0:
            print('Please go away and stop eating my sheep')
            break
        else:
            print(f'Oi! Sheep number {i}! You are about to be eaten by a wolf!')
            break
