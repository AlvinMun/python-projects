print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
road = input('You\'re at a crossroad. Where do you want to go?\nType "left" or "right": ').lower()
if road == "left":
    wait = input('You\'ve come to a lake. There is an island in the middle of the lake.\nType "wait" to wait for a boat. Type "swim" to swim across: ').lower()
    if wait =="wait":
        room = input("You arrived at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which color do you choose: ").lower()
        if room == "red":
            print("It's a room full of fire. Game over!")
        elif room == "yellow":
            print("You found the treasure! You win!")
        else:
            print("You enter a room of beasts. Game over!")
    else:
        print("You get attacked by an angry shark. Game over!")
else:
    print("You fell into a hole. Game over!")
