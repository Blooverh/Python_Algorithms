
from LinkedLists.QueueLinkedList import LinkedQueue

def merge(S1, S2, S):
    """Merge 2 sorted queue instances S1 and S2 into empty queue S"""

    while not S1._isEmpty() and not S2._isEmpty():
        if S1.first() < S2.first():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue(S2.dequeue())

    while not S1._isEmpty():
        S.enqueue(S1.dequeue()) # add remaining elements from S1

    while not S2._isEmpty():
        S.enqueue(S2.dequeue()) # add remaining elements from S2

def merge_sort(S):
    """Sort the elements of queue S using the merge sort algorithm"""

    n = len(S)

    if n < 2:
        return # list is already sorted 
    
    #divide 
    # any other queue implementation can be used (std python queue implementation)
    S1 = LinkedQueue()
    S2 = LinkedQueue()

    while len(S1) < n//2:
        S1.enqueue(S.dequeue()) # move the first n//2 elements to S1

    while not S._isEmpty(): #move the rest to S2
        S2.enqueue(S.dequeue())

    # conquer with recursion
    merge_sort(S1)
    merge_sort(S2)

    #merge results 
    merge(S1, S2, S)

toBeMergedList = LinkedQueue()
array = [85, 24, 63, 45, 17, 31, 96, 50]
for i in range(len(array)):
    toBeMergedList.enqueue(array[i])

# for i in range(len(toBeMergedList)):
#     print(toBeMergedList.dequeue())

merge_sort(toBeMergedList)

for i in range( len(toBeMergedList)):
    print(toBeMergedList.dequeue())


