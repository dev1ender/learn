class Solution:
    def __init__(self) -> None:
        self.mem=[]
        self.N=0

    def recursion(self,weight,arr,first)->int:
        if(len(arr)==0):
            return weight
        if(self.mem[first][self.N] > -1):
            return self.mem[first][self.N]
        self.mem[first][self.N] = weight + max(self.recursion(arr[0],arr[2:],first+2) ,self.recursion(weight,arr[1:],first+1))
        return self.mem[first][self.N] 
    
    def rob(self, nums) -> int:
        self.N = len(nums)
        self.mem = [ [ -1 for y in range( self.N+1 ) ] for x in range( self.N+1 ) ]
        return self.recursion(0,nums,0)
        

solution =  Solution();
print(solution.rob([1,2,1,1]))