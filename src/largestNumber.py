# Given an integer n, return the largest 
# number that contains exactly n digits.
# Problem Link: https://app.codesignal.com/arcade/code-arcade/intro-gates/SZB5XypsMokGusDhX/description

def largestNumber(n):
    res = []
    for i in range(n):
        res.append('9')
    return int(''.join(res))
