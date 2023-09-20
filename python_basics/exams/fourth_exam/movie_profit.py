movie = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
percentage = int(input())
percentage /= 100

total = days * tickets * ticket_price
total -= total * percentage

print(f'The profit from the movie {movie} is {total:.2f} lv.')
