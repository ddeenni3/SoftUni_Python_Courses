cards = input().split(' ')
shuffle_counts = int(input())

halved_deck = len(cards) // 2
cards_left_half = cards[:halved_deck:]
cards_right_half = cards[halved_deck::]

combined_deck = [' '] * len(cards)

for shuffle in range(shuffle_counts):
    counter = 1
    if shuffle > 0:
        cards_left_half = combined_deck[:halved_deck:]
        cards_right_half = combined_deck[halved_deck::]
    while counter < len(cards) + 1:
        if counter % 2 == 0:
            combined_deck[counter - 1] = cards_right_half.pop(0)
        else:
            combined_deck[counter - 1] = cards_left_half.pop(0)
        counter += 1

print(combined_deck)