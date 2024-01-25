number_of_pieces = int(input())

album = {}

for piece in range(number_of_pieces):
    current_piece, composer, key = input().split('|')
    album[current_piece] = {'composer': composer, 'key': key}

while True:
    command = input().split('|')
    if command[0] == 'Stop':
        break
    elif command[0] == 'Add':
        piece, composer, key = command[1], command[2], command[3]
        if piece not in album.keys():
            album[piece] = {'composer': composer, 'key': key}
            print(f'{piece} by {composer} in {key} added to the collection!')
        else:
            print(f'{piece} is already in the collection!')
    elif command[0] == 'Remove':
        piece = command[1]
        if piece in album.keys():
            del album[piece]
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
    elif command[0] == 'ChangeKey':
        piece, new_key = command[1], command[2]
        if piece in album.keys():
            album[piece]['key'] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

for piece in album:
    print(f'{piece} -> Composer: {album[piece]["composer"]}, Key: {album[piece]["key"]}')
