fav_book = input()
current_book = input()

found_book = False

book_counter = 0

while current_book != 'No More Books':
    if current_book == fav_book:
        found_book = True
        print(f'You checked {book_counter} books and found it.')
        break
    book_counter += 1
    current_book = input()

if not found_book:
    print('The book you search is not here!')
    print(f'You checked {book_counter} books.')