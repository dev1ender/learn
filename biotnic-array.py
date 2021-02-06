def function(A,B):    
    n = len(A)
    if(n==0):
        return -1
    if(n==1):
        if(B==A[0]):
            return 0
        else:
            return -1
    if(n>1):
        return recursion(A,0,n-1,B)
        
def recursion(A,first,last,B):
    middle = (last-first)%2
    if(A[first]==B):
        return first
    elif A[last]==B:
        return last
    elif A[middle]==B:
        return middle
    # update first and last
    if(A[first]<A[middle]):
        pass
    return recursion(A,first,last,B)


A = [5, 6, 7, 8, 9, 10, 3, 2, 1]
B = 10
function(A,B)