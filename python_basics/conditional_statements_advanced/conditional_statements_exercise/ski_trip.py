time_of_stay = int(input())
accommodation = input()
review = input()
price = 0

if accommodation == 'room for one person':
    price += (time_of_stay - 1) * 18
elif accommodation == 'apartment':
    price += (time_of_stay - 1) * 25
    if time_of_stay < 11:
        price *= 0.7
    elif 11 <= time_of_stay <= 16:
        price *= 0.65
    else:
        price *= 0.50
elif accommodation == 'president apartment':
    price += (time_of_stay - 1) * 35
    if time_of_stay < 11:
        price *= 0.9
    elif 11 <= time_of_stay <= 16:
        price *= 0.85
    else:
        price *= 0.80

if review == 'positive':
    price *= 1.25
elif review == 'negative':
    price *= 0.90

print(f'{price:.2f}')
