def square_area(a):
    if a < 0:
        raise ValueError("if either number was negative")
    return a*a

print(square_area(3))