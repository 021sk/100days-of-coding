print("welcom to treasure island")
print("your mission  to find treasure")
choice1 = input('you are at crossroad where do you want togo: "left", "right" \n').lower()
if choice1 == "left":
    second_choice = input("there is beach on the right and you"
                          " should chose that you want to 'wait' or 'swim': ").lower()
    if second_choice == "wait":
            third_choice = input(
            "right choice, now a boat take care of you but there are three doors, which one do you pick?"
            " 'red' or 'yellow' or 'blue' : ").lower()
            if third_choice == "red":
                print("You picked the right one, the treasure is there, YOU WINE")
            elif third_choice == "yellow":
                print("You picked the wrong, Game Over!")
            elif third_choice == "blue":
                print("You picked the wrong, Game Over!")
            else:
                print("You picked the wrong, Game Over!")
                
         
    else :
        print("game over")
    
else :
    print("game over")