class Employee:
    
    a=1


class Programmer(Employee):
    b=2


class Manaager(Programmer):
    c=4    

o=Employee()
print(o.a)    # prints the the a attribute
# print(o.b) shows an error as there is no b attribute in employee class
o=Programmer()
print(o.a,o.b)

o=Manaager()
print(o.a,o.b,o.c)