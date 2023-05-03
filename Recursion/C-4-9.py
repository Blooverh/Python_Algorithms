def minMax(list, length):
   if(length ==1):
      return list[0]
   return max(list[length-1], minMax(list, length-1))

list=[2,5,2,3,8,9,3,1]

print(minMax(list, len(list)))