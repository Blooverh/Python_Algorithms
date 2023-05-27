from queue import Empty
import DoublyLinkedList
"""Inheritance of the class DoublyLinkedList """
class LinkedDeque(DoublyLinkedList):
    """Double ended queue implementation based on a doubly linked list """

    def first(self):
        """Return but do not remove the element at the front of the deque"""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element
    
    def last(self):
        """return but do not remove the element at the back of the deque"""

        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element
    
    def insert_first(self, e):
        """Add element to front of the list"""
        self._insert_between(e, self._header, self._header._next) #after header since header node is always null (None)

    def insert_last(self, e):
        """Add element behind tail"""
        self._inser_between(e, self._trailer._prev, self._trailer) #before tail node

    def delete_first(self):
        """Remove and return the element from the front of the deque"""

        if self.is_empty():
            raise Empty("Deque is empty")
        
        return self._delete_node(self._header._next)
    
    def delete_last(self):
        """Remove and return the element at the end of the dequeue"""
        if self.is_empty():
            raise Empty("Deque is empty")
        
        return self._delete_node(self._trailer._next)