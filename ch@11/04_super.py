class Employee:
    def __init__(self):
        print("constructor of employee")
    a=1


class Programmer(Employee):
    def __init__(self):
        print("constructor of employee")
    b=2


class Manaager(Programmer):
    def __init__(self):
        super().__init__()#it will run the parent constructor when this constructor run
        print("constructor of employee")
    c=4    

# o=Employee()
# print(o.a)    # prints the the a attribute
# print(o.b) shows an error as there is no b attribute in employee class
# o=Programmer()
# print(o.a,o.b)

o=Manaager()
print(o.a,o.b,o.c)