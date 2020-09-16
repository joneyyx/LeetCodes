# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_length = float('inf')
        for word in strs:
            if len(word) < min_length:
                min_length = len(word)
                min_word = word

        for i in range(len(min_word)):
            for word in strs:
                if min_word[i] != word[i]:
                    return min_word[:i]
        return min_word