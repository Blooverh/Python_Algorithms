"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by
rearranging the letters of a different word or phrase, typically using all the original letters exactly once."""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        words={}

        for char in s:
            words[char]= words.get(char, 0)+1
            
        
        for char in t: 
            if char in words:
                words[char]-=1
                if words[char] == 0:
                    words.pop(char)
        print(words)
        return len(words) ==0 
    
