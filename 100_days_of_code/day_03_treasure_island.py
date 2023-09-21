print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input('You arrive at a crossroad. Left or Right? (L/R): ').lower()

if direction == 'l':
    choice = input('You are now in front of a lake. Swim to get to the other side quicker or'
                   ' Wait for a boat to arrive safer.(S/W): ').lower()
    if choice == 'w':
        last_choice = input('You are faced by 3 doors - Red, Yellow and Blue. Only one will lead you to the treasure'
                            ' and the rest will curse you into the void. Choose wisely. (R/Y/B) ').lower()
        if last_choice == 'r':
            print('You were burned by fire and perished into the doom.\nGame Over.')
        elif last_choice == 'b':
            print('You were feast upon by beasts. May your bones rest in peace.\nGame Over.')
        elif last_choice == 'y':
            print('The treasure awaits you.\nCongratulations!\nYou Win!')
        else:
            print('Game Over.')
    else:
        print('You were attacked and eaten by a trout.\nGame Over.')
else:
    print('You fall into a hole.\nGame Over.')
