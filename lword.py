# Program to find the length of the longest word in a list
# Function iterates through each word and tracks the maximum length

def find_longest_word(words):
    """Find the length of the longest word in a list"""
    # Initialize maximum length to 0
    maxlength = 0
    
    # Iterate through each word and update max length if current word is longer
    for word in words:
        if len(word) > maxlength:
            maxlength = len(word)
    return maxlength 

# Sample list of words
words = ["apple", "banana", "cherry", "watermelon", "kiwi"]

# Call function and display result
print("the length of the longest word is :", find_longest_word(words))