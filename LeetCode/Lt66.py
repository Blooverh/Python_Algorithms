from collections import UserList
def plusOne(digits: UserList[int]) -> UserList[int]:
    number=0
    for num in digits:
        number= number * 10 + num

    stringNum= str(number+1)
    listNum=[]
    for char in stringNum:
        listNum.append(int(char))

    return listNum

print(plusOne([1,2,3]))