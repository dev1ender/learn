def longestPalindrome( s: str) -> str:
  res = s[0]
  n = len(s)
  for middle in range(n):
      left = middle-1
      right = middle+1
      while (left >= 0 and right < n):
          if s[left] != s[right]:
              break
          res = s[left:right+1]
          left-=1
          right+=1
  return res
                
s = "babad"
longestPalindrome(s)