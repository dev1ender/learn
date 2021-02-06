class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        return [[1 + max(abs(i), abs(j)) for j in range(-A + 1, A)] for i in range(-A + 1, A)]


solution = Solution()
res = solution.prettyPrint(3)
print(res)

# 3 3 3 3 3 
# 3 2 2 2 3 
# 3 2 1 2 3 
# 3 2 2 2 3 
# 3 3 3 3 3 
