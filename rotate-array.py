def rotateMatrix(A):
    size  = len(A)
    B = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            B[i][j] = A[size-j-1][i]
    return B

rotateMatrix([[1, 2],[3, 4]])