

import random

name=input("input your name: ")
num=int(input("player choice between 1-3 "))
mylist=["#","Rock","Paper","Scissor"]
choice=mylist[num]
print(f"{name} choice is {choice}")

com=random.randint(1,3)
comp_choice=mylist[com]
print("computer choice is "+comp_choice)

if choice=="Rock" and comp_choice== "Paper":
    print("RockVsPaper")
    print("Computer is winner")

elif choice=="Paper" and comp_choice== "Rock":
    print("PaperVsRock")
    print("player is winner")

elif choice=="Rock" and comp_choice== "Scissor":
    print("RockVsScissor")
    print("Player is winner")
elif choice=="Scissor" and comp_choice== "Rock":
    print("ScissorVsRock")
    print("Computer is winner")

elif choice=="Scissor" and comp_choice== "Paper":
    print("ScissorVsPaper")
    print("Player is winner")
elif choice=="Paper" and comp_choice== "Scissor":
     print("PaperVsScissor")
     print("Computer is winner")
else:
    print("Match Draw")









