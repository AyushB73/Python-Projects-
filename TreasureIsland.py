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
direction = input('Where do you want to go ? Type "left" or "right".\n').lower()
if direction == "left" :
    lake = input('You\'ve come to a lake.'
                 'Do you want to "swim" or "wait for boat"\n').lower()
    if lake == "wait":
        door = input("You arrived at island unarmed."
                     "There is a house with 3 doors."
                     "One red,One Yellow,One Blue."
                     "Which Color do you Choose.\n").lower()
        if door == "red":
            print("Room full of fire.Game Over")
        elif door == "blue":
            print("Room full of beasts.Game Over")
        elif door == "yellow":
            print("You found the Treasure.You win!")
        else :
            print("You chose an invalid door.Game Over.")

    else :
        print("You got attacked by Trout.Game Over")
else :
    print("You fell in to a hole. Game Over.")
