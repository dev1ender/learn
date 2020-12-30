import sys

def appearsNBy3(arr, n):
    count1 = 0
    count2 = 0
    first = sys.maxsize
    second = sys.maxsize
    for i in range(0, n): 
        if (first == arr[i]):
            count1 += 1
        elif (second == arr[i]):
            count2 += 1
        elif (count1 == 0):
            count1 += 1
            first = arr[i]
        elif (count2 == 0):
            count2 += 1
            second = arr[i]
        else:
            count1 -= 1
            count2 -= 1
    count1 = 0
    count2 = 0
    for i in range(0, n): 
        if (arr[i] == first):
            count1 += 1
        elif (arr[i] == second):
            count2 += 1
    if (count1 > n / 3):
        return first
    if (count2 > n / 3):
        return second
    return -1


arr = [4, 2, 3, 4, 4 ]
n = len(arr) 
print(appearsNBy3(arr, n))