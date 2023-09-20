stay_length = int(input())
room_type = input()
review = input()

price = 0

if room_type == 'room for one person':
    price = (stay_length - 1) * 18
elif room_type == 'apartment':
    price += (stay_length - 1) * 25
    if stay_length < 10:
        price *= 0.7
    elif stay_length <= 15:
        price *= 0.65
    else:
        price *= 0.5
elif room_type == 'president apartment':
    price += (stay_length - 1) * 35
    if stay_length < 10:
        price *= 0.9
    elif stay_length <= 15:
        price *= 0.85
    else:
        price *= 0.8

if review == 'positive':
    price *= 1.25
elif review == 'negative':
    price *= 0.9

print(f'{price:.2f}')
