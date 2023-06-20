import os 
# print(os.path.getsize(path))
# print(os.path.isdir(path))
# print(os.listdir(path))

def disk_usage(path):
    total= os.path.getsize(path) #account for direct usage 
    if os.path.isdir(path): #if this path is a directory
        for filename in os.listdir(path): #then for each child
            childpath=os.path.join(path,filename) #compose full path to children 
            total += disk_usage(childpath) # add childs size to total

    print('{0:7}'.format(total), path)
    return total

disk_usage('C:/Users/diogo/OneDrive/Desktop/Python_Algorithms/Recursion')