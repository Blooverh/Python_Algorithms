"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""
from collections import UserList
class Solution:
    def groupAnagrams(self, strs: UserList[str]) -> UserList[UserList[str]]:

        hashmap = {}
        
        for word in strs:
            # we sort the word so we can append it as a key because all words that are anagrams when sorted are the same
            sortedWords= ''.join(sorted(word)) 

            if sortedWords not in hashmap:
                hashmap[sortedWords] = [word] # value is a list that will contain the word
            else:
                hashmap[sortedWords].append(word) #if key exists we append the current word
        
        ans= [] # list that will contains all the lists of anagrams

        for value in hashmap.values():
            ans.append(value)
        
        return ans
 

test=Solution()

list=["eat","tea","tan","ate","nat","bat"]

print(test.groupAnagrams(list))
                