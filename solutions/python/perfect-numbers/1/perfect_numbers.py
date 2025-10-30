def classify(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    addition = 0
    for i in range(1, number):
        if number%i == 0:
            addition += i
            
    if addition < number:
        return "deficient"
    elif addition == number:
        return "perfect"
    else:
        return "abundant"
        
            