import sys 

data=[]
n=10
for k in range(n):
    a= len(data) # number of elements
    b= sys.getsizeof(data) # actual size in bytes 
    print('Length:{0:3d}; Size in bytes:{1:4d}'.format(a,b))
    data.append(None) # increase length by one by appending None (Null) on every kth position of the list data

"""In the array, we can reference the same object 4 times in memory allocations, thus the increase of 32 bytes every 4th element
in the array"""
"""Because a list is a referential structure, the result of getsizeof function for a list instance only includes 
the size for representing its primary structure; does not account for memory used by the object itself that are elements of the list.
Meaning each object at ith position in the array has its own memory size along with the memory size of its reference in the array."""
print(data)