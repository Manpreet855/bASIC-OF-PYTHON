def removedd(l,word):
    n=[]
    for item in l:
        l.remove(word)
        return l
    
l=["preet","reet","geeta","harry","jerry","an"]    
print(removedd(l,"reet"))

# pennnndddiiinnnggggg 
# chaeck hh.py

def remove_and_strip(word_list, word_to_remove):
    # Remove extra spaces and filter out the given word
    return [item.strip() for item in word_list if item.strip() != word_to_remove]

# Example usage
words = ["  apple ", " banana ", "orange", " apple", " grape "]
result = remove_and_strip(words, "apple")
print(result)  # Output: ['banana', 'orange', 'grape']
