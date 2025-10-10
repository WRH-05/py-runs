def is_armstrong_number(number):
    number_str=str(number)
    n= len(number_str)
    total=0
    for i in number_str:
        total+= int(i)**n
    return total == number