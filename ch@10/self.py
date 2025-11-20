class employee:
    language="py" #this is a class attribute
    salary=1200000

    def getinfo(self):
        print(f" The language is{self.language}.")# self writing is import in this


preet=employee() 
preet.language="javascript" #this is a instance attribute  
print(preet.salary,preet.language)
preet.getinfo() #This is an instance attribute
# employee.getinf(preet)