
# from typing import List
# import math

def matrix_chain(d):
    """ d is a list of n+1 numbers such that size of kth matrix
    id d[k] by d[k+1]
    
    Return a n by n table such that N[i][j] represents the min number
    of multiplications needed to compute the product of Ai through Aj inclusive"""

    n = len(d) - 1  # number of matrices
    N = [[0] * n for i in range(n)]  # initilialize n by n result to 0

    for b in range(1, n): #number of products in subchain
        for i in range(n-b): # start of subchain
            j = i + b
            N[i][j] = min(N[i][k] + N[k+1][j] + d[i] * d[k+1] * d[j+1] for k in range(i, j))
    
    return N #or N[0][n-1]
# A leetcode solution
# def minScoreTriangulation( A: List[int]) -> int:
#     SP, L = [[0]*50 for _ in range(50)], len(A)
#     for i in range(2,L):
#         for j in range(L-i):
#             s, e, SP[s][e] = j, j + i, math.inf
#             for k in range(s+1,e): SP[s][e] = min(SP[s][e], A[s]*A[k]*A[e] + SP[s][k] + SP[k][e])
#     return SP[0][L-1]

array = [2,3,4]
print(matrix_chain(array))
# print(minScoreTriangulation(array))