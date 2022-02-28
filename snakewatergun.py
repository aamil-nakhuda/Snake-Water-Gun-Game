import random

lst=["s","w","g"]

my_points=0
computer_points=0
chances=10
rounds=0

print("Enter s for snake\nEnter w for water\nEnter g for gun \nPress r to restart")

while rounds!=10:
    my_input=input()
    computer_input=random.choice(lst)

    if my_input=="s" and computer_input=="w":
        my_points+=1
        print(f"Your input is {my_input} and computers is {computer_input}\nYour point is {my_points} and computers is {computer_points}")
        
    elif my_input=="w" and computer_input=="g":
        my_points+=1
        print(f"Your input is {my_input} and computers is {computer_input}\nYour point is {my_points} and computers is {computer_points}")
    elif my_input=="g" and computer_input=="s":
        my_points+=1
        print(f"Your input is {my_input} and computers is {computer_input}\nYour point is {my_points} and computers is {computer_points}")
    elif my_input=="w" and computer_input=="s":
        computer_points+=1
        print(f"Your input is {my_input} and computers is {computer_input}\nYour point is {my_points} and computers is {computer_points}")
    elif my_input=="g" and computer_input=="w":
        computer_points+=1
        print(f"Your input is {my_input} and computers is {computer_input}\nYour point is {my_points} and computers is {computer_points}")
    elif my_input=="s" and computer_input=="g":
        computer_points+=1
        print(f"Your input is {my_input} and computers is {computer_input}\nYour point is {my_points} and computers is {computer_points}")
    elif my_input==computer_input:
        print(f"Your input is {my_input} and computers is {computer_input}\nYour point is {my_points} and computers is {computer_points}")
    else:
        print("Invalid Input")
    rounds+=1

if my_points>computer_points:
    print(f"\nYOU WON THE GAME :) !\nYour point is {my_points} and computers is {computer_points}\nGAME INVENTED BY AAMIL!")
elif my_points<computer_points:
    print(f"\nYOU LOST THE GAME :( !\nYour point is {my_points} and computers is {computer_points}\nGAME INVENTED BY AAMIL!")
else:
    print("ITS A DRAW!")
