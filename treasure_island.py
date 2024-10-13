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
direction = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right': \n" )
if direction == "left":
    action = input("You've come to a lake. There is a island in the middle of the lake. Type 'wait' to wait for a boat or 'swim' to swim across: \n")
    if action == "wait":
        door_color = input("You arrive at the island unharmed. There is a house with three doors- one red, one blue and one yellow. Which color do you choose: \n")
        if door_color == "red":
            print("You entered a room full of fire and got burned. Game Over.")
        elif door_color == "blue":
            print("You entered a room full of beasts and got eaten. Game Over")
        elif door_color == "yellow":
            print("You found the treasure. You Win!")
        else:
            print("You entered the wrong input. Game Over")
    else:
        print("You got eaten by a trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")