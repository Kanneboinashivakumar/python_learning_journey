import math
def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(x)
def power(base, exponent):
    return math.pow(base, exponent)
def factorial(n):
    if n < 0:
        raise ValueError("Cannot compute factorial of a negative number.")
    return math.factorial(n)