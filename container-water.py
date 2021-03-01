def maxArea(arr):
  max_area = 0
  n = len(arr)
  L, R  = 0, n-1
  while L<=R:
    local_max = (R-L)*min(arr[L],arr[R])
    max_area = local_max if local_max > max_area else max_area
    if arr[L] <= arr[R]:
      L+=1
    else:
      R-=1
  return max_area

s = [4,3,2,1,4]
maxArea(s)