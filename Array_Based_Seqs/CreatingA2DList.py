def matrix(r,c):
    """create a list of c amount of 0's for an index in range of 0 to value of rows"""
    """creates a list of c amount of 0's for an amount of r rows"""
    data=[[0] * c for j in range(r)]
    print(len(data[0])) # gives length of elements in columns
    print(len(data)) # gives length of rows / length of the lists inside the list 
    return data

print(matrix(4,3))