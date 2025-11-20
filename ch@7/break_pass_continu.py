# for i in range(100):
#     if(i==55):
#         break # Exit the loop right now.
#     print(i)
for i in range(90):
    pass # It instructs to “do nothing”.

# skip one value in this 
for i in range(70):
    if(i==55):
        continue # skip this iteration or value
    print(i)    
    
# skip multipal values
for i in range(50):
    if i in (34,35,36): # skip these values
        continue
    print(i)

    