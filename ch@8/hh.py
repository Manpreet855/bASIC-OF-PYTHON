def remove_and_strip(word_list, word_to_remove):
    return [item.strip() for item in word_list if item.strip() != word_to_remove]

# Get input from the user
words = input("Enter words separated by commas: ").split(",")
word_to_remove = input("Enter the word you want to remove: ")

# Process and display the result
result = remove_and_strip(words, word_to_remove)
print("Updated list:", result)
