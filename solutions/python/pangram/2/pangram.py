def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    
    # Extract only letters from the sentence and convert to a set
    letters_in_sentence = {char for char in sentence if char.isalpha()}
    
    return letters_in_sentence == alphabet