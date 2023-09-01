from LinkedLists.QueueLinkedList import LinkedQueue

def quick_sort(S):
    """Sort the elements of queue S using the quick sort algorithm"""
    n = len(S)

    if n < 2: # list is already sorted
        return 
    
    #divide 
    p = S.first() # using first element as the pivot
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()

    while not S.is_empty():
        if S.first() < p:
            L.enqueue(S.dequeue()) # enqueue element if less than pivot by dequeueing current element in S
        elif S.first() > p:
            G.enqueue(S.dequeue()) # enqueue element if greater than pivor by dequeueing current element in S
        else: # S.first() must be equal to Pivot
            E.enqueue(S.dequeue())

    #conquer (with recursion)
    quick_sort(L) # sort elements less than P on current L linked List in a recurisve way
    quick_sort(G) # sort elements greater than P on current L linked List in a recurisve way

    #concatenate results
    while not L._isEmpty():
        S.enqueue(L.dequeue())

    while not E._isEmpty():
        S.enqueue(E.dequeue())

    while not G._isEmpty():
        S.enqueue(G.dequeue())

    