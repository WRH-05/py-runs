def is_triangle(sides):
    a, b, c = sorted(sides)
    return a > 0 and a + b >= c

def equilateral(sides):
    if is_triangle(sides):
        return sides[0] == sides[1] == sides[2]
    return False

def isosceles(sides):
    if is_triangle(sides):
        return sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]
    return False

def scalene(sides):
    if is_triangle(sides):
        return sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]
    return False