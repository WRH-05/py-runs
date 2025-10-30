import math as m

def score(x, y):
    current_radius = m.sqrt(x**2 + y**2)

    if current_radius <= 1:
        return 10
    elif current_radius <= 5:
        return 5
    elif current_radius <= 10:
        return 1
    else:
        return 0