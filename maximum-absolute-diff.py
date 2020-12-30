def maxArr( A):
        minIndex=0
        maxIndex =0
        for i in range(1,len(A)):
            if(A[maxIndex]<A[i]):
                maxIndex = i
            if(A[minIndex]>A[i]):
                minIndex = i
        return abs(A[maxIndex]-A[minIndex])+abs(maxIndex-minIndex)

print(maxArr([1,3,9,3,2,]))
    