# The code below supposed to solve quadratic equation
# Link to problem: https://app.codesignal.com/challenge/xnPdLDQ7gR6pobqFe?solutionId=4kJWLXX6yoSbknHqH

from math import sqrt

def quadraticEquation(a, b, c):
    det = b**2 - 4 * a * c
    res = []
    if det >= 0:
        x1 = (-b + sqrt(det))/(2 * a)
        x2 = (-b - sqrt(det))/(2 * a)
        if x1 == x2:
            return [x1]
        res.append(x1)
        res.append(x2)
        res.sort()
        return res
    return res
