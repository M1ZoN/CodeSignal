# Problems on logic:

# Given n and firstNumber, find the number which
# is written in the radially opposite position to firstNumber.
# E.g For n = 10 and firstNumber = 2, the output should be 7.

def circleOfNumbers(n, firstNumber):
    return (n // 2 + firstNumber) % n

# Using the bike's timer, calculate the current time. 
# Return an answer as the sum of digits that the digital 
# timer in the format hh:mm would show.
# For n = 240, the output should be 4.
# Since 240 minutes have passed, the current time is 04:00. 
# The digits sum up to 0 + 4 + 0 + 0 = 4, which is the answer.

def lateRide(n):
    h = list(str(n // 60))
    m = list(str(n % 60))
    if len(h)<2:
        h.append('0')
    if len(m)<2:
        m.append('0')    
    return int(h[0])+int(h[1])+int(m[0])+int(m[1])

# Some phone usage rate may be described as follows:
# first minute of a call costs min1 cents,
# each minute from the 2nd up to 10th (inclusive) costs min2_10 cents
# each minute after 10th costs min11 cents.
# You have s cents on your account before the call. What is the duration 
# of the longest call (in minutes rounded down to the nearest integer) you can have?

def phoneCall(min1, min2_10, min11, s):
    sum = 0
    if s >= min1:
        sum += 1
        s -= min1
    if s >= min2_10 and sum == 1:
        while sum < 10 and s - min2_10 >= 0:
            sum += 1
            s -= min2_10
    if s >= min11 and sum == 10:
        while s - min11 >= 0:
            sum += 1
            s -= min11
    return sum
