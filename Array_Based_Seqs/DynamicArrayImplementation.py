"""The key is to provide means to grow the Array A that stores all the elements of a list.
When an array is full and we append an element to the list we have to create a new array and copy 
the elements of previous array to the new array """

import ctypes # provides low-level arrays 

class DynamicArray:
    """A dynamic array class akin to a simplified Python list"""

    def __init__(self):
        """Create an empty array"""
        self._n=0 #count actual elements
        self._capacity=1 #default array capacity 
        self._A= self._make_array(self.capacity) #low level array creation with capaity one containing nothing.

    def __len__(self):
        """Return the number of elements stored in the array"""
        return self._n
    
    def __getitem__(self, k): # k is the position in the array where we will get the elements that is in that storage position (k).
        if not 0<=k <self._n:
            raise IndexError('Invalid Index')
        return self._A[k] #retrieve from array
    
    def append(self, obj):
        """Add object to the end of the array"""
        if self._n == self._capacity: # if not enough room
            self._resize(2*self._capacity) #double the capacity of the array
        self._A[self._n]= obj
        self._n +=1

    def _resize(self, c): #nonpublic utity
        """Resize the internal capacity of the array to c"""
        B= self._make_array(c) # creation of new bigger array

        for k in range(self._n): #for each existing value 
            B[k]=self._A[k] 
            
        self._A=B #use the bigger Array as the new reference 
        self._capacity=c

    def _make_array(self, c):
        """Retrun new array with capacity c"""
        """ctypes.py_object is a data type in the library that represents a generic python object as a C language object """
        return (c* ctypes.py_object) () #Check ctypes documentation. function with no arguments is returned.

list=DynamicArray._make_array(list , 3)

print(list.__len__())
print(list.append(10))
print(list.__getitem__(2))