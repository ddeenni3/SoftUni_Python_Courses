movie = input()
hall_type = input()
tickets_sold = int(input())

tickets_price = 0

if movie == 'A Star Is Born':
    if hall_type == 'normal':
        tickets_price += tickets_sold * 7.5
    elif hall_type == 'luxury':
        tickets_price += tickets_sold * 10.5
    elif hall_type == 'ultra luxury':
        tickets_price += tickets_sold * 13.5
elif movie == 'Bohemian Rhapsody':
    if hall_type == 'normal':
        tickets_price += tickets_sold * 7.35
    elif hall_type == 'luxury':
        tickets_price += tickets_sold * 9.45
    elif hall_type == 'ultra luxury':
        tickets_price += tickets_sold * 12.75
elif movie == 'Green Book':
    if hall_type == 'normal':
        tickets_price += tickets_sold * 8.15
    elif hall_type == 'luxury':
        tickets_price += tickets_sold * 10.25
    elif hall_type == 'ultra luxury':
        tickets_price += tickets_sold * 13.25
elif movie == 'The Favourite':
    if hall_type == 'normal':
        tickets_price += tickets_sold * 8.75
    elif hall_type == 'luxury':
        tickets_price += tickets_sold * 11.55
    elif hall_type == 'ultra luxury':
        tickets_price += tickets_sold * 13.95
print(f'{movie} -> {tickets_price:.2f} lv.')
