# Ticket numbers usually consist of an even number of digits. 
# A ticket number is considered lucky if the sum of the first 
# half of the digits is equal to the sum of the second half.
# Given a ticket number n, determine if it's lucky or not.
# Problem Link: https://app.codesignal.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ/description


def isLucky(n):
    num = str(n)
    sum1 = 0
    sum2 = 0
    size = len(num) // 2
    for i in range(0, size):
        sum1 += int(num[i])
    for i in range(size, len(num)):
        sum2 += int(num[i])
    return sum1==sum2
