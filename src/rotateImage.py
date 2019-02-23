# You are given an n x n 2D matrix that represents an
# image. Rotate the image by 90 degrees (clockwise).
# Problem Link: https://app.codesignal.com/interview-practice/task/5A8jwLGcEpTPyyjTB

def    rotateImage(a):
    newArr = []
    for i in range(len(a)):
        temp = []
        for j in range(len(a), 0, -1):
            temp.append(a[j-1][i])
        newArr.append(temp)
    return newArr
            

print(rotateImage([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]))