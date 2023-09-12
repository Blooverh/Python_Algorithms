""" Longest Common Subsequence """

def LCS(X,Y):
    """ return a table such that L[j][k] is 
    length of LCS for X[0: J], Y[0: K]"""

    n= len(X)
    m = len(Y)

    L=[[0] * (m+1) for k in range(n+1)] # matrix filled with 0s

    for j in range(n):
        for k in range(m):
            if X[j] == Y[k]: #align this match
                L[j+1][k+1] = L[j][k]+1
            else:
                L[j+1][k+1] = max(L[j][k+1], L[j+1][k]) #choose to ignore one character

    return L 


array1= ['G', 'T', 'T', 'C', 'C', 'T', 'A', 'A', 'T', 'A']
# array2= ['C', 'G', 'A', 'T', 'A', 'A', 'T', 'T', 'G', 'A', 'G', 'A']
array2= ['C', 'G', 'T', 'T', 'C', 'C', 'T', 'A', 'A', 'T', 'A', 'A']


sol = LCS(array1, array2)
# print(LCS(array1, array2))

def LCS_solution(X,Y,L):
    """Return the longest commong subtring of X and Y, given LCS Table L"""

    solution=[]

    j = len(X)
    k = len(Y)

    while L[j][k] > 0:
        if X[j-1] == Y[k-1]:
            solution.append(X[j-1])
            j-=1
            k-=1
        elif L[j-1][k] >= L[j][k-1]:
            j-=1
        else:
            k-=1

    return ''.join(reversed(solution))

print(LCS_solution(array1, array2, sol))