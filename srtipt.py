import sys

class Solution:
  def thirdLar(self,arr):
    res = [-sys.maxsize,-sys.maxsize,-sys.maxsize]
    for i in arr:
      if i > res[2] and not res[0]==i and not res[1]==i:
        if i > res[1] and not res[0]==i:
          if i > res[0]:
            res.insert(0,i) 
            res.pop(3) # arr len become 4
          else:
            res.insert(1,i)
            res.pop(3)
        else:
          res[2] = i
    print(res)
    return res[2]



arr =  [5,0,-1,2,-3,1] # 2
obj = Solution()
result = obj.thirdLar(arr)
print(result)