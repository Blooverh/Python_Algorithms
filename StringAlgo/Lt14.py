
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs: #if empty list return empty string
            return ""

        common_prefix = ""
        for i, char in enumerate(strs[0]):
            for word in strs[1:]:
                if i >= len(word) or word[i] != char: 
                    return common_prefix
            common_prefix += char

        return common_prefix