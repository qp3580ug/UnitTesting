import math


def triangle_area(height, base):

    if height < 0 or base < 0:
        raise ValueError('Base and height must be positive')

    return height * base * 0.5

def circle_area(radius):

    if radius < 0:
        raise ValueError
    return radius ** 2 * math.pi