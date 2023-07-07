"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""
from collections import UserList
class Solution:
    def groupAnagrams(self, strs: UserList[str]) -> UserList[UserList[str]]:

        dict= {} #temp dict for checker

        answer=[] #answer list that will contain the temp list 

        temp=[]
        if len(strs) <= 1:
            items=temp.append(strs[0])    

            return answer.append(items)

        for i in range(len(strs)):

            for j in range(len(strs)):
                temp.append(strs[i])
                for ch in strs[i]:
                    if ch not in dict:
                        dict[ch]=1
                    else:
                        dict[ch] +=1
                
                for c in strs[j]:
                    if c in dict:
                        dict[c]-=1
                
                print(dict)
                dict={}
                # for c in dict:
                #     if dict[c] != 0 or c not in dict:
                #         dict={}
                #     else:
                #         temp.append(strs[j])
                # answer.append(temp)
                # temp=[]                    
                # dict={}
        
        return answer


                       
            
            
            

test=Solution()

list=["eat","tea","tan","ate","nat","bat"]

print(test.groupAnagrams(list))
                