limit = 7
movie_counter = 0


winner_points = 0
winner_movie = ''


while True:
    current_points = 0
    command = input()
    if command == 'STOP':
        break

    for char in command:
        current_points += ord(char)
        if 97 <= ord(char) <= 122:
            current_points -= 2 * len(command)
        elif 65 <= ord(char) <= 90:
            current_points -= len(command)

    if current_points > winner_points:
        winner_points = current_points
        winner_movie = command
    movie_counter += 1
    if movie_counter == 7:
        print(f'The limit is reached.')
        break

print(f'The best movie for you is {winner_movie} with {winner_points} ASCII sum.')
