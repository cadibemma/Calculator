import math


def addition(a, b):
    a = int(a)
    b = int(b)
    return a + b


# def subtraction(a, b):
#     a = int(a)
#     b = int(b)
#     return b - a
#
#
# def multiplication(a, b):
#     a = int(a)
#     b = int(b)
#     return a * b
#
#
# def division(a, b):
#     a = float(a)
#     b = float(b)
#     return b / a
#
#
# def square(a):
#     a = int(a)
#     return math.pow(a, 2)
#
#
# def square_root(a):
#     a = float(a)
#     return math.sqrt(a)


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result
