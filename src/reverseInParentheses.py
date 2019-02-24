# Write a function that reverses characters in 
# (possibly nested) parentheses in the input string.
# Input strings will always be well-formed with matching ()s.
# Problem Link: https://app.codesignal.com/arcade/intro/level-3/9DgaPsE2a7M6M2Hu6/description

def reverseInParentheses(inputString):
    newArr = list(inputString)
    count = 0
    ind = []
    i = 0
    while i < len(newArr):
        if newArr[i] == '(':
            ind.append(i)
        elif newArr[i] == ')':
            newS = newArr[ind[len(ind)-1]+1:i]
            newS.reverse()
            newArr = newArr[:ind[len(ind)-1]]+newS[:]+newArr[i+1:]
            ind.pop()
            i -= 2
        i += 1
    return ''.join(newArr)
