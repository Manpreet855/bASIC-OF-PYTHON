a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
if(b==0):
    raise ZeroDivisionError("hey our program is not meant to  divide number by Zero")
else:
    print(f" the  division a/b is {a/b}")