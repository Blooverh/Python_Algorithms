"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """create a dictionary where he hold each letter as a key and its occurrences as a value"""
        hashmap= {} 
        counter=0
        #base case
        if len(s) != len(t):
            return False
        #main cases
        for ch in s:
            if ch not in hashmap:
                hashmap[ch] =1 
            else:
                hashmap[ch] +=1

        for ch in t:
            if ch in hashmap:
                hashmap[ch] -=1
        
        for ch in hashmap:
           if hashmap[ch] != 0:
               return False

        return True
            

test= Solution()
print(test.isAnagram("anagram","nagaram"))