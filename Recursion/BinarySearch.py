def binarySerch(list, number, low, high) -> int:
    
    #Non recursive way
    # low=0
    # high=len(list)
    # while low < high:
    #     mid=int((low+high)/2)
    #     if number > list[mid]:
    #         low=mid
    #     elif number == list[mid]:
    #         return mid 
    #     else:
    #         high=mid

    if low >high:
        return 0
    else:
        mid=(low+high)//2
        if number == list[mid]:
            return mid
        elif number > list[mid]:
            return binarySerch(list, number, mid+1, high)
        else:
            return binarySerch(list, number, low, mid-1)

list=[2,4,7,18, 45,56,130]
answer= binarySerch(list, 45, 0, len(list))
print(answer)