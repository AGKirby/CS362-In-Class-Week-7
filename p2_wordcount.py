def wordcount(string):
    letters = False #if there is a word
    words = 0 
    for char in string:
        if((char == " ") and letters): #if there is a word followed by a space
            letters = False #end of the word
            words += 1
        elif(not letters and (char.isalpha() or char.isnumeric())): #if the beginning of a word
            letters = True
    if(letters): #last word is not terminated by a space
        words += 1
    return words
