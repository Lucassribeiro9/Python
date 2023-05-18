def mult(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

print(mult(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))