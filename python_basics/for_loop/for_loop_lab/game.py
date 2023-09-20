import random

words = ('python', 'softuni', 'държава', 'куче', 'home')
max_guesses = 5
response_condition = False

print('Welcome to Softuni PB Game!')
print('You have to unscramble the word', max_guesses, 'guesses')

word = random.choice(words)
scrambled_word = ''.join(random.sample(word, len(word)))

for guess in range (max_guesses):
    print('Scrambled word:', scrambled_word)
    answer = input('Enter your guess')

    if answer == word:
        print('Congratulations! You have unscrambled the word!')
        response_condition = True
        break
    else:
        print('Try again!')
if not response_condition:
    print('Sorry, you ran out of guesses. The word was:', word)

