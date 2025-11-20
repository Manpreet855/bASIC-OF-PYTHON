class employee:
    language="py" #this is a class attribute
    salary=1200000

preet=employee() 
preet.language="javascript" #this is a instance attribute  
print(preet.salary,preet.language)
# Note: Instance attributes, take preference over class attributes during assignment & retrieval. 