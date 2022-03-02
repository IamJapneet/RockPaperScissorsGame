#This Code was written by Japneet on March 2, 2022. Thank You for Reading.

from operator import truediv
import random

def gamewin(computer,you):
    if computer==you:
        return None

    elif computer=='Rock':
        if you=='Paper':
            return False
        elif you=='Scissors':
            return True 
    elif computer=='Scissors':
        if you=='Paper':
            return False
        elif you=='Rock':
            return True
    elif computer=='Paper':
        if you=='Rock':
            return False
        elif you=='Scissors':
            return True
print("Computer turn:Rock, Paper, Scissors?")
random_num=random.randint(1,3)
if random_num == 1:
    computer='Rock'
elif random_num == 2:
    computer='Paper'
elif random_num == 3:
    computer='Scissors'

you=input("Your Turn:Rock, Paper, Scissors?\n")
a=gamewin(computer, you)

print(f"Computer chose {computer}")
print(f"You chose {you}")

if a==None:
    print("The game is a tie!")
elif a:
    print("Congrats🎉 You Won!")
else:
    print("Oh No! You Lose!")

