def is_valid(isbn):
    isbn = isbn.replace("-", "")
    
    if len(isbn) != 10:
        return False

    total = 0

    for index, char in enumerate(isbn):
        if char == "X" and index == 9:
            value = 10
        elif char.isdigit():
            value = int(char)
        else:
            return False
        
        multiplier = 10 - index
        total += value * multiplier

    return total % 11 == 0
