class Employee:
    
    salary=125
    increment= 15
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment =(( salary/self.salary)-1)*100 


e=Employee()
print(e.salaryAfterIncrement)
# print(e.increment)
# amount=int(input("Enter your salary:"))