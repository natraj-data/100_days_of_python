print(
    '''
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''
)

print("Welcome to Treasure Island")

print("Your mission is to find out the treasure")

choice1 = input(
    "You're at the cross road. Where do you wanna go? Type \"left\" or \"right\" :\n").lower()

if choice1 == "right":
    print("Your choice was right but your car crashed. You lost...")
else:
    print("You have reached the lake..There is an island in the middle of the lake. Hopefully you can find your treasure in the island")
    choice2 = input(
        "Do you wanna wait for the boat or swim: Type \"wait\" or \"swim\" :\n").lower()
    if choice2 == "swim":
        print("OMG: Fell into the Anaconda's trap..You are dead.. ")
    else:
        print("You have reached the island.. I guess you are gonna grab the treasure...")
        choice3 = input(
            "There are three colorful doors to open: Type R for Red, G for green or B for Blue : \n").lower()
        if choice3 == "r":
            print("Room full of fire....You burned..")
        elif choice3 == "g":
            print(
                "Congrats: You win... There is a treasure...Huge crown and Sparkling ring...")
        elif choice3 == "b":
            print("Your bad: You become a prey for the violent animal beast...")
        else:
            print("Invalid door choice...You lost this time.. Try again..")
