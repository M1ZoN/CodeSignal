# This program takes two strings, and finds the number of common characters between them.
# E.g if you have commonCharacterCount("aabcc", "adcaa")  the output should be 3
# because Strings have 3 common characters - 2 "a"s and 1 "c".
# problem link: https://app.codesignal.com/arcade/intro/level-3/JKKuHJknZNj4YGL32

def commonCharacterCount(s1, s2):
    newArr = []
    for i in s1:
        if i in s2:
            index = s2.index(i)
            s2 = s2[:index] + s2[index+1:]
            newArr.append(i)
    return len(newArr)
