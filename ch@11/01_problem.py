class TwoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"the vector is {self.i}i + {self.j}j ")

class ThreeDvector(TwoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j) 
        self.k=k      
    def show(self):
        print(f"the vector is {self.i}i + {self.j}j + {self.k}k")

print("\n Enter the values for 2d vector:" )

i_2d=int(input("Enter the i: "))
j_2d=int(input("Enter the j: "))

a=TwoDvector(i_2d,j_2d)
print("\n Enter the values for 3d vector:" )
i=int(input("Enter the i: "))
j=int(input("Enter the j: "))
k=int(input("Enter the k: "))
b=ThreeDvector(i,j,k)       
a.show()
b.show()