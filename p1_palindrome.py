def palindrome(string):
    standardized = ""
    for char in string: #only get letters, change to capitals
        if(char.isupper()):
            standardized += char
        elif(char.islower()):
            standardized += char.upper() #convert to uppercase
    backwards = standardized[::-1]  #reverse string by starting at the end and going backwards (-1)
    if(backwards == standardized): #if spelled the same forward and backwards
        return True #is a palindrome
    return False #not a palindrome
