# This function takes an array of strings and returns an array of longest strings
# E.g allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]) will return ["aba", "vcd", "aba"]
# Link to the problem: https://app.codesignal.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL/description

def allLongestStrings(inputArray):
    longest = len(inputArray[0])
    for i in inputArray:
        if len(i) > longest:
            longest = len(i)
    res = []
    for i in inputArray:
        if len(i) == longest:
            res.append(i)
    return res
