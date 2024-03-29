def merge(S1, S2, S):
    """Merge 2 sorted python lists S1 and S2 into a properly sized list S"""

    i=0
    j=0

    while i+j < len(S):
        if j == len(S1) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i] # copy ith element of S1 as next item of S
            i+=1
        else:
            S[i+j]= S2[j] # copy jth element of S2 as next item of S
            j+=1

def merge_sort(S):
    """Sort the elements of S using the merge-sort algorithm"""

    n= len(S)
    if n < 2:
        return 
    
    #divide
    mid = n // 2
    
    S1 = S[0:mid] #copy first half
    S2 = S[mid: n] #copy second half

    #conquer
    merge_sort(S1) # sort copy of first half
    merge_sort(S2) # sort copy of second half

    #merge results 

    merge(S1, S2, S) #merge sorter halves back into S

    return S

array = [85, 24, 63, 45, 17, 31, 96, 50]

print(merge_sort(array))