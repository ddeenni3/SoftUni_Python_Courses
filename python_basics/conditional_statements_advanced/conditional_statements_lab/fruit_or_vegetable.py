user_input = input()

fruit_or_vegetable = 'unknown'

if user_input in ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']:
    fruit_or_vegetable = 'fruit'
elif user_input in ['tomato', 'cucumber', 'pepper', 'carrot']:
    fruit_or_vegetable = 'vegetable'

print(fruit_or_vegetable)
