# first and last elem and sum of middle elem should be equal
# problem link: https://app.codesignal.com/challenge/7kZavbM3FBC85FtNA

def isSmooth(arr):
    return (arr[0]==arr[len(arr)-1] == ((arr[len(arr)//2] + arr[len(arr)//2 - 1]) if len(arr) % 2 == 0 else arr[len(arr)//2]))
