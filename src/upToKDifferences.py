# Given a string str and an integer k, your task is to 
# split str into a minimal possible number of substrings 
# so that there are no more than k different symbols in 
# each of them. Return the minimal possible number of 
# such substrings.

def upToKDifferences(str, k):
	diff = 0
	temp = []
	count = 0
	for i in str:
		if i not in temp:
			diff += 1
		if diff > k:
			temp = []
			diff = 1
			count += 1
		temp.append(i)
	if temp:
		count += 1
	return count