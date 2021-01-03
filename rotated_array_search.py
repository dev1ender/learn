""" Rotated Sorted Array Search """

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        n = len(A)-1
        first  = 0
        last = n 
        mid  = int(n/2)
        while mid < last:
            if (A[first] == B):
                return first
            elif(A[last]==B):
                return last
            elif(A[mid]==B):
                return mid
            if A[first] > A[last]:
                # pivot in middle
                if( A[mid] < A[last] and A[mid] < B and A[last] > B):
                    first = mid+1
                elif(A[mid] > A[first] and A[mid] > B and A[first] < B):
                    last= mid-1
                elif(A[mid] < A[last]):
                    last = mid - 1
                elif(A[mid] > A[last]):
                    first = mid + 1
            elif A[first] <  A[last]:
                # sorted arr
                if A[mid] > B:
                    last = mid-1
                elif A[first] < B:
                    first = mid+1
            mid = first + int((last-first)/2)
        return -1
solution = Solution()
print(solution.search([ 186, 192, 193, 202, 204, 2, 3, 6, 10, 11, 12, 17, 21, 28, 29, 30, 31, 32, 37, 38, 39, 40, 41, 47, 49, 50, 51, 52, 55, 57, 58, 59, 60, 65, 67, 68, 71, 72, 74, 77, 78, 80, 82, 83, 88, 89, 90, 94, 100, 107, 108, 109, 111, 112, 114, 115, 116, 118, 119, 121, 123, 124, 126, 129, 133, 134, 135, 137, 138, 144, 147, 148, 150, 151, 154, 156, 159, 161, 163, 165, 166, 167, 168, 169, 174, 178, 180, 182, 183, 185 ],143))