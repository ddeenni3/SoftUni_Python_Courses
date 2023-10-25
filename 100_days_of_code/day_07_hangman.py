import random

# create lists containing different words for the word choices

capitals = ['Sofia', 'Brasilia', 'Cairo', 'Berlin', 'Paris', 'London', 'Ankara', 'Havana', 'Amsterdam', 'Vienna']
animals = ['elephant', 'rabbit', 'hippopotamus', 'cheetah', 'giraffe', 'gorilla', 'ostrich', 'reindeer', 'rhinoceros']
fruits = ['banana', 'apple', 'watermelon', 'pineapple', 'strawberry', 'coconut', 'avocado']
vegetables = ['pepper', 'onion', 'potato', 'lettuce', 'asparagus', 'celery', 'broccoli']


# create functions for the main loop


def choose_word(some_list: list):
    return random.choice(some_list)


def choose_category():
    maximum_guesses = int(input('Please enter max guesses count: '))
    while True:
        user_choice = input('Please select a category:\n1. Capitals\n2. Animals\n3. Fruits\n4. Vegetables\n')
        if user_choice == '1':
            word = choose_word(capitals)
            break
        elif user_choice == '2':
            word = choose_word(animals)
            break
        elif user_choice == '3':
            word = choose_word(fruits)
            break
        elif user_choice == '4':
            word = choose_word(vegetables)
            break
        else:
            print('Invalid input. Please try again')
    return word, maximum_guesses


# create main function


def main():
    game_over = False
    current_word, max_guesses = choose_category()
    current_word = [x for x in current_word]
    display = ['_'] * len(current_word)
    print(f'psst the word is {"".join(current_word)}')
    while True:
        current_guess = input('Letter to try: ')
        if current_guess in [x.lower() for x in display]:
            print(f'You have already guessed {current_guess}\nPlease try another letter.')
            continue
        if current_guess not in [x.lower() for x in current_word]:
            max_guesses -= 1
            print(f'Remaining guesses {max_guesses}')
            if max_guesses == 0:
                print(f'You ran out of guesses\nThe word was: {current_word}')
                break
        else:
            for pos, letter in enumerate(current_word):
                if letter.lower() == current_guess.lower():
                    display[pos] = letter
                    if '_' not in display:
                        print(f'You won!\nThe word is {"".join(display)}')
                        game_over = True
                        break
            if game_over:
                break
        print("".join(display))


main()
