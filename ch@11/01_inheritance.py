class Emlopyee:
    company="ITC"
    name="Default name"
    language="python"
    def show (self):
        print(f"the name is { self.name} and the company is {self.company}")

# class coder:
#     language="python"
#     def printlanguage(self):
#         print(f"out of the languages here is your language:{self.language}")
# class programmer:
#     company="ITC infotech"
#     def show(self):
#         print(f" the name is { self.name} and the company is {self.company}")

#     def showLanguage(self):
#         print(f"The name {self.name} and he is good with {self.Language} language")            
class programmer(Emlopyee):
    company="ITC infotech "
    def showLanguage(self):
        print(f"The name {self.name} and he is good with {self.language} language")



a=Emlopyee()  
b=programmer()
# print(a.company,b.company)        
b.show()
# b.printlanguage()
b.showLanguage()