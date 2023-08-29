import math

def merge(src, result, start, inc):
    """Merge src[start: start + inc] and src[start+inc: start+2*inc] into result"""

    end1 = start + inc #boundary for run 1
    end2 = min(start + 2*inc, len(src)) # boundary for run 2

    x,y,z= start, start+inc, start #index into run1, run2, result

    while x < end1 and y< end2:
        if src[x] < src[y]:
            result[z]= src[x] # copy from run 1 and increment x
            x+=1
        else:
            result[z] = src[y] # copy from run2 and increment y
            y+=1 

        z+=1

    if x< end1:
        result[z: end2]= src[x: end1] #copy remainder of run 1 output
    elif y < end2:
        result[z: end2]= src[x: end2] #copy remainder of run 2 output

def merge_sort(S):
    """Sort the elements of python list using the merge sort algorithm non recursive"""

    n= len(S)
    logn = math.ceil(math.log(n,2))

    src, dest= S, [None] * n #make temporary storage for dest

    for i in (2**k for k in range(logn)): #pass i creates all runs of length 2*i
        for j in range(0, n, 2*i): #each passes merges 2 length i runs
            merge(src, dest, j, i)
        
        src, dest = dest, src #reverse roles of lists

    if S is not src: 
        S[0:n] = src[0:n] #additional copy to get results ot S