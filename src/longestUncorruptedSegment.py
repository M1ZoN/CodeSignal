# Given the content of the source and the migrated content of the target, 
# find the length and the starting block of the longest uncorrupted data segment (segment = subsequent blocks).
# Problem Link: https://app.codesignal.com/company-challenges/purestorage/vfaESus49J4N9JHim

def longestUncorruptedSegment(sourceArray, destinationArray):
    ind = 0
    longest = 0
    ongoing = 0
    res = []
    for i in range(len(sourceArray)):
        if sourceArray[i] == destinationArray[i]:
            ongoing += 1
        else:
            if ongoing > longest:
                longest = ongoing
                ind = i - longest
            ongoing = 0
    if ongoing > longest:
        longest = ongoing
        ind = len(sourceArray) - longest
    res.append(longest)
    res.append(ind)
    return res
