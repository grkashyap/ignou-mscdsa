# Input string from user
text = input("Enter a string: ")

# Count characters (including spaces)
char_count = len(text)

# Count blanks (spaces)
blank_count = text.count(' ')

# Count words
# split() separates words based on spaces
word_count = len(text.split())

# Display results
print("Number of characters:", char_count)
print("Number of blanks (spaces):", blank_count)
print("Number of words:", word_count)