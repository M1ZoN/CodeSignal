# You are given an array of integers a. A new array b is generated 
# by rearranging the elements of a in the following way:

# b[0] is equal to a[0];
# b[1] is equal to the last element of a;
# b[2] is equal to a[1];
# b[3] is equal to the second-last element of a;
# and so on.
# Your task is to determine whether the new array b is sorted
# in strictly ascending order or not.

def alternatingSort(a):
    b = [None]*len(a)
    beg = 0
    last = len(a) - 1
    for i in range(len(a)):
        if i % 2 == 0:
            b[i] = a[beg]
            beg += 1
        else:
            b[i] = a[last]
            last -= 1
    for i in range(len(b)-1):
        if b[i] >= b[i+1]:
            return False
    return True