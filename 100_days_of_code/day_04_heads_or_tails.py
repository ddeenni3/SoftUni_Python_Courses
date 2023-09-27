import random


def head_tails():
    current_try = random.randint(0, 1)
    if current_try == 1:
        return 'Heads'
    return 'Tails'


print(head_tails())