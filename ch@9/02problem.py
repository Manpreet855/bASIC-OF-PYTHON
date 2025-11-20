import random

def gameeee():
    print("you are are playing game..")
    
    score =random.randint(1,75)
   
    with open("highscore.txt") as f:
         highscore=f.read()
    if(highscore!=""):
            highscore=int(highscore)
    else:
            highscore=0
        

    print(f"your score:{score}")
    if(score>highscore ):
        print("new highscore!")
        #  write this highscore in to the file
        with open("highscore.txt","w") as f:
            f.write(str(score))
    
    return score
gameeee()