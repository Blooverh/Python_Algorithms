
from collections import UserList 
def maxProfit(prices: UserList[int]) -> int:

    ProfitIfSoldToday=0 
    lsf =float('inf')
    profit=0

    for i in range(len(prices)):
        
        if prices[i] < lsf:
            lsf = prices[i]
        
        ProfitIfSoldToday= prices[i] - lsf

        if profit < ProfitIfSoldToday:
            profit = ProfitIfSoldToday

    return profit 

list=[7,1,5,3,6,4]

print(maxProfit(list))

