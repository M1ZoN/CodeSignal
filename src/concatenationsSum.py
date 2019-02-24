# Given an array of positive integers a, your task is 
# to calculate the sum of every possible a[i] ∘ a[j], 
# where a[i] ∘ a[j] is the concatenation of the string 
# representations of a[i] and a[j] respectively.

def concatenationsSum(a):
    sum = 0
    for i in range(len(a)):
        for j in range(len(a)):
            prod = str(a[i]) + str(a[j])
            sum += int(prod)
    return sum