# Problems on logic:

# Given n and firstNumber, find the number which
# is written in the radially opposite position to firstNumber.
# E.g For n = 10 and firstNumber = 2, the output should be 7.

def circleOfNumbers(n, firstNumber):
    return (n // 2 + firstNumber) % n
