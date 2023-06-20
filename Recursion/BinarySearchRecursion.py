def binarySearch(array, target, low, high):

    """return true if target is found """
    if low > high:
        return False
    else:
        mid= (low+high)//2 #find pivot of list 
        if target == array[mid]: 
            return True
        elif target < array[mid]: #if target less than pivot, high is now element before mid
            return binarySearch(array, target, low, mid-1)
        else: #if target higher than pivot, low is now 
            return binarySearch(array, target, mid+1, high)
"""This recursion decreases size of the array until there is only one element which is (low, high and mid)
either the element we want returning True or False if element not between low and high"""
array= [1,2,3,4,5,6,7,8,9]
target =0

print(binarySearch(array, target, 1, 9))