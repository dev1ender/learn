def threeSum(arr):
    arr.sort()
    n = len(arr)
    res = []
    for i,a in enumerate(arr):
      if i > 0 and a == arr[i-1]:
        continue
      l , r = i+1 , n-1
      while l < r:
        sum = a+arr[l]+arr[r]
        if(sum>0):
          r-=1
        elif(sum<0):
          l+=1
        else:
          res.append([a,arr[l],arr[r]])
          l+=1
          while arr[l] == arr[l-1] and l<r:
            l+=1
    return res
arr = [-1,0,1,2,-1,-4]
threeSum(arr)