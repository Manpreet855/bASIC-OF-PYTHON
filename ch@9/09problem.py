with open("this.txt") as f:
    content1=f.read()

with open("myfile.txt") as f:
    content2=f.read()

if(content1==content2):
    print("yes these fles are identical")

else:
    print("No these fles are not identical")    