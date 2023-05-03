"""Insertion sort runs at O(n^2) due to the nested loops
for an unordered list."""
def insertion_Sort(A):
    """Sort list of comparable elements into ascending order"""

    for k in range(1, len(A)):
        curr=A[k] #current element to be inserted 
        j=k #find correct index j for current
        #while A[j-1] > than curr (A[j]) we swap leftwards until A[j-1] <curr
        while j >0 and A[j-1]>curr: #element A[j-1] must be after current
            A[j]=A[j-1]
            j-=1 #current index that was swapped that will hold the current element we used for comparison 
        A[j]=curr #current goes now to the right index
        #And we iterate the loop with again with the next kth element.
    
    return A

list=[2,1,5,3,7,8,4]
print(insertion_Sort(list))