# This program sorts without touching -1 numbers
# E.g sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]) will return [-1, 150, 160, 170, -1, -1, 180, 190]
# Problem Link: https://app.codesignal.com/arcade/intro/level-3/D6qmdBL2NYz49XHwM/description

def sortByHeight(a):
    s = []
    indices = []
    for i in range(0,len(a)):
        if a[i] != -1:
            s.append(a[i])
            indices.append(i)
    s.sort()
    for i,j in zip(range(0,len(indices)),range(0, len(s))):
        a[indices[i]] = s[j]
    return a
