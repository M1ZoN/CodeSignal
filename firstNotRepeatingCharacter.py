# Given a string s consisting of small English letters, 
# find and return the first instance of a non-repeating
# character in it. If there is no such character, return '_'.
#Problem link: https://app.codesignal.com/interview-practice/task/uX5iLwhc6L5ckSyNC/description

def firstNotRepeatingCharacter(s):
    res = '_'
    for i in range(len(s)):
        newArr = s[:i]+s[i+1:]
        if s[i] not in newArr:
            return s[i]
    return res
