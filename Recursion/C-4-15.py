def subsetPrint(list):

    #If list is equal to an empty list return the empty list as a sublist (subset)
    if list == [] :
        return [[]]

    """ """
    return [[list[0]]+y for y in subsetPrint(list[1:])] +subsetPrint(list[1:])

print(subsetPrint([3,2,1]))

#Non recursive LeetCode 78

def subsets(list):
    output=[[]]

    for i in list:
        output+= [lst + [i] for lst in output]
    
    return output

print(subsets([3,2,1]))