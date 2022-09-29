
from ast import If, Pass


def game_view(row1,row2,row3):
    print("our game view")
    print(row1)
    print(row2)
    print(row3)

def chose_place():
    chose=" "
    while chose not in range(0,9):
        chose=int(input("enter where you wanted to place: "))
        if chose not in range(0,9):
            print("chose again: ")
        
    return chose

def update(list1,list2,list3,pos):
    user_value=input("enter 'X' or 'O' : ")
    if pos in range(0,3):
        list1[pos]= user_value
        return list1
    elif pos in range(3,6):
        if pos==3:
            list2[0]=user_value
            return list2
        elif pos==4:
            list2[1]=user_value
            return list2
        else:
            list2[2]=user_value
            return list2
    else:
        if pos==6:
            list3[0]=user_value
            return list3
        elif pos==7:
            list3[1]=user_value
            return list3
        else:
            list3[2]=user_value
            return list3
        

"""def game_on():
    chose=" "
    while chose not in ("Y", "N"):
        chose=input("enter WANT TO PLAY OR NOT: ")
        if chose not in ("Y", "N"):
            print("chose again: ")
    
    if chose=="Y":
        return True
    
    else: 
        return False"""

def winner(game_list1,game_list2,game_list3):
    if (game_list1[0]==game_list1[1]==game_list1[2]=="X" or game_list1[0]==game_list1[1]==game_list1[2]== "O") or (game_list1[0]==game_list2[0]==game_list3[0]=="X" or game_list1[0]==game_list2[0]==game_list3[0]== "O") or (game_list1[0]==game_list2[1]  ==game_list3[2]=="X" or game_list1[0]==game_list2[1]  ==game_list3[2]=="O") or (game_list2[0]==game_list2[1]==game_list2[2]=="X" or game_list2[0]==game_list2[1]==game_list2[2]=="X" "O") or (game_list3[0]==game_list3[1]==game_list3[2]=="X" or game_list3[0]==game_list3[1]==game_list3[2]== "O") or (game_list1[1]==game_list2[1]==game_list3[1]=="X" or game_list1[1]==game_list2[1]==game_list3[1]== "O") or (game_list1[2]==game_list2[2]==game_list3[2]=="X" or game_list1[2]==game_list2[2]==game_list3[2]=="O") or (game_list1[2]==game_list2[1]==game_list3[0]=="X" or game_list1[2]==game_list2[1]==game_list3[0]== "O"):
        return True
    else:
        return False
        




game_list1=[" "," "," "]
game_list2=[" "," "," "]
game_list3=[" "," "," "]

#game_ontheway=True

game_view(game_list1,game_list2,game_list3)
w=False
while w==False:
   #game_view(game_list1,game_list2,game_list3)
   s=chose_place()
   update(game_list1,game_list2,game_list3,s)
   game_view(game_list1,game_list2,game_list3)
   w=winner(game_list1,game_list2,game_list3)
   if w==True:
    print("Winner")
    break
   #game_ontheway=game_on()










