'''
1 for sanke
-1 for water
0 for gun

'''
#  alway think to import funcations and dica in program or take help from chat Gpt or google . what to import

import random  

print("choose 's' for sanke 'w' for water 'g' for gun")
computer= random.choice([1,-1,0])
youstr=input("Enter your choice:")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"sanke",-1:"water",0:"gun"}
you=youDict[youstr]
print(f"You chose '{reverseDict[you]}'\ncomputer chose '{reverseDict[computer]}'")
if(computer==you):
    print("Its a draw")
else:    
    if(computer==-1 and you==1):
        print("you win!")
    elif(computer==-1 and you==0):
        print("you losee!")
    elif(computer==1 and you==-1):
        print("you lose!")
    elif(computer==1 and you==0):
        print("you win!")
    elif(computer==0 and you==-1):
        print("you win!")
    elif(computer==0 and you==1):
        print("you lose!")
    else:
        print("something went wrong!")    
