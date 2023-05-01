def game_main():
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

    direction = input("\nYou are at a crossroad. Type 'L' to go left or 'R' to go right: ")

    if direction != "L":
        print("You fell into a hole.\nGame Over!")
        return
    
    direction = input("\nYou are in front of a river and you see a trout.\n\
                      Type 'S' to swim across or 'W' to wait until the trout leaves: ")

    if direction != "W":
        print("The trout attacked you and killed you.\nGame Over!")
        return 
    
    direction = input("\nYou see 3 doors ahead of you:\n\
                      A Red door, a Yellow door and a Blue door.\n\
                      Type 'R' to enter the Red door, 'Y' for the Yellow door or 'B' for the Blue door.\n")

    if direction == "Y":
        print("Congratulations! You have found the treasure!\nYOU WIN!!")
    elif direction == "R":
        print("You are burned by fire.\nGame Over!")
    elif direction == "B":
        print("Your are eaten by beasts.\nGame Over!")
    else:
        print("Game Over!")

    return 

if __name__ == "__main__":
    game_main()