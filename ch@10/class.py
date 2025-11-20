class employee:
    language="py" #  this is a class attribute
    salary=1200000

preet=employee()    
print(preet.salary,preet.language)
manpreet= employee()#  this is a instance attribute
manpreet.name = "Manpreet Sidhu"
print(manpreet.salary,manpreet.name)
# here name is a instance attribute and salary and language are class attributes as they belong to the class