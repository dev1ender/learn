class Solution:
    def canJump(self, nums) -> bool:
      maximum = 0
      for index,item in enumerate(nums):
        if index <= maximum and item + index > maximum:
          maximum = item + index
      return True if maximum >= len(nums)-1 else False
      

# nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
obj = Solution()
obj.canJump(nums)