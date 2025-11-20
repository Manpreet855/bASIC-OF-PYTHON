class employee:
    language="py" #this is a class attribute
    salary=1200000
    name="preet"
    def getinfo(self):
        print(f" The language is {self.language}.")# self writing is import in this


    def __init__(self,name,salary):#duner method which is automatically called
        self.name=name
        self.salary=salary
        print("im creating objcet")  
preet=employee("Manpreet",1220000) 
preet.language="javascript" #this is a instance attribute  
print(preet.salary,preet.language,preet.name)
preet.getinfo() 