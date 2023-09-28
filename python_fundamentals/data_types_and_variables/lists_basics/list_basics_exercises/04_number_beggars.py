coins = input().split(', ')
beggars = int(input())

coins_as_integers = list(map(int, coins))

coins_per_beggar = [0] * beggars

current_beggar = 0

for coin in coins_as_integers:
    coins_per_beggar[current_beggar] += coin
    current_beggar = (current_beggar + 1) % beggars

print(coins_per_beggar)
