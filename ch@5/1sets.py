s=set()
# do not use s={} as it will create an empty dictionary
s = {1,2,23,4,4,4,"preet"}
# no repetition allowed! 
s.add(1) 
s.add(2)  
print(s, type(s))