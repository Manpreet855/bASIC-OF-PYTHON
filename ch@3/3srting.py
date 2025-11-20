# len () function – This function returns the length of the strings. 
str = "harry" 
print(len(str))  # Output: 5 

print(str.endswith("rry"))  # Output: True 
# String.endswith("rry") – This function_ tells whether the variable string ends with 
# the string "rry" or not. If string is "harry", it returns true for "rry" since Harry ends with rry. 
# string.count("c") – counts the total number of occurrences of any character. 
count = str.count("r") 
print(count)  # Output: 2 
# the first character of a given srting
capitalized_string = str.capitalize() 
print(capitalized_string)  # Output: "Harry"
# string.find(word) – This function friends a word and returns the index of first occurrence of that word in the string. 
str = "harry" 
index = str.find("rr") 
print(index)  # Output: 2 