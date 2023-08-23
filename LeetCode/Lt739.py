from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """No stack solution runs very slow"""
        # difference=[0] * len(temperatures) #emty list that will contain number of days it will take to get warmer 

        # #base 
        # if len(temperatures) <=1:
        #     difference[0] = 0
        #     return difference
        
        # for i in range(len(temperatures)):
        #     sum=0
        #     j= i + 1
        #     while j < len(temperatures):
        #         sum+=1

        #         if temperatures[i] < temperatures[j]:
        #             difference[i] = sum
        #             sum=0
        #             break
                
        #         j+=1
                
                 

        # return difference

        stack=[]
        difference=[0] * len(temperatures)
        
        for i, currentTemp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < currentTemp:
                unsettledDay= stack.pop()
                difference[unsettledDay] = i - unsettledDay

            stack.append(i)

        return difference

array= [73,74,75,71,69,72,76,73]
sol = Solution()
print(sol.dailyTemperatures(array))