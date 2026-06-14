def find_longest_word(words):
    
    maxlength = 0
    for word in words:
        if len(word)>maxlength:
            maxlength = len(word)
    return maxlength 

words = ["apple", "banana", "cherry", "watermelon", "kiwi"]
print("the length of the longest word is :", find_longest_word(words))