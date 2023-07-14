from collections import heapq
from LinkedLists import PositionalList 
import PriorityQueue 
def pq_sort(C):
    """Sort a collection of elements stored in a Positional List"""
    n= len(C)
    P= PriorityQueue() 

    for i in range(n):
        element= C.delete(C.first())
        P.add(element, element) #use element as key and value 

    for j in range(n):
        (k,v)= P.remove_min()
        C.add_last(v) #store smallest remaining element in C 