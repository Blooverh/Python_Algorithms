# def is_even(k):
#     if (k % 2) == 0:
#         return True
#     else:
#         return False
    
# k=int(input("What number you want to check? "))
# print(f"Is {k} an even number")
# answer= is_even(k)
# print(answer)

"""Without using mathematical operators"""
def isEven(k):
    evenList=[]
    for num in range(2,1000,2):
        evenList.append(num)

    if k in evenList:
        return True
    else:
        return False

print(isEven(6))
