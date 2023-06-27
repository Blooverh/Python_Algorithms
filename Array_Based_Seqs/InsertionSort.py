"""Insertion sort runs at O(n^2) due to the nested loops
for an unordered list."""
def insertion_sort(A):
# sort list of comparable elements into a non decreasing order

    for k in range(1, len(A)): # we start from 1 as 1st element (at index 0) is seen as sorted
        curr= A[k] # current stores value of element k to be inserted in correct position
        curr_idx = k # j stores current index
    
        while curr_idx > 0 and A[curr_idx -1] > curr:
            A[curr_idx] = A[curr_idx -1]
            curr_idx -= 1
            
    A[curr_idx] = curr

    return A

list=[2,1,5,3,7,8,4]
print(insertion_sort(list))