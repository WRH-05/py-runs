def rotate(text, key):

    result = ""
    
    for char in text:
        if char.islower():
            index = ord(char) - 97 
            shifted = (index + key) % 26 
            new_char = chr( shifted + 97) 
            result += new_char 
        elif char.isupper(): 
            index = ord(char) - 65 
            shifted = (index + key) % 26
            new_char = chr( shifted + 65)
            result += new_char 
        else:
            result += char
    return result