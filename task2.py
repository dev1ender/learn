# size m * n , k=3
# 1  2  3
# 2  3  4 
# 2  4  6  can because 2 < 3 
# 2  4  6 
# 2  4  6 

# log(m)*log(n)
# o(m* log(n)) worst case 
# bin serach first col  strictly gratern than k 


def recurse(first,last,arr,k):
  if first >= last:
    return -1
  mid = first + (last - first) // 2
  if arr[mid]==k:
    return mid
  if arr[first]==k:
    return first
  if arr[last]==k:
    return last
  if k > arr[mid]:
    first = mid+1
  else:
    last = mid-1
  return recurse(first,last,arr,k)

def binarySearch(arr,k):
  return recurse(0,len(arr)-1,arr,k)

def solution(arr,k):
  res = tuple()
  for rowIndex,row in enumerate(arr):
    if row[0] < k and row[-1]>k:
      colIndex  = binarySearch(row, k )
      if colIndex>-1:
        res = (rowIndex,colIndex)
        break
  return res

mat = [ [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 37, 39, 50] ]
res = solution(mat,37)
print(res)
#  ---- code test for recursion as asked:
# arr = [1,3,4,5,6]
# k = 6
# index= binarySearch(arr, k )
# print(index)



