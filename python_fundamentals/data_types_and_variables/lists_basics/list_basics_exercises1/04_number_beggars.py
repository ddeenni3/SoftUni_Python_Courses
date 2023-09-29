list_of_coins = input().split(', ')
number_of_beggars = int(input())

collected = []

current_beggar = 0

for beggar in range(number_of_beggars):
    current_beggar_sum = 0
    for coin in range(current_beggar, len(list_of_coins), number_of_beggars):
        current_beggar_sum += int(list_of_coins[coin])
    collected.append(current_beggar_sum)
    current_beggar += 1


# for coin in list_of_coins:
#     current_beggar_sum = 0
#     current_beggar_sum += int(coin)
#     collected[current_beggar] += current_beggar_sum
#     current_beggar = (current_beggar + 1) % number_of_beggars

print(collected)


