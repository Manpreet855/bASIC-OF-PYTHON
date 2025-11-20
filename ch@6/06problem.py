markes=int(input("Enter your markes:"))
if markes<0 or markes>100:
    print("Invaild markes! Please enter a value between 0 and 100.")

exit() # we this to  stop function immediately in the program execution so programe not continue for second if statement

if(markes==100 and markes>90):
    grade="Ex"
elif (markes<90  and markes>80):
     grade=  "A"
elif(markes<80  and markes>70):
    grade= "B"
elif(markes<70  and markes>60):
    grade= "C"
elif(markes<60  and markes>50):
    grade= "D"
elif(markes<50  ):
    grade= "F"

   
print("your grade is: ", grade)







