#
# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


# 首先判断长度
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict = {}
        for c in t:
            dict[c] = dict.get(c, 0) +1
        for c in s:
            if c in t:
                dict[c] = dict[c] -1
        for value in dict.values():
            if value != 0:
                return False
        return True

s=Solution()
print(s.isAnagram("a", "b"))

#方法2， 排序
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         #return True if list(s).sort()==list(t).sort() else False
#         return True if sorted(s)==sorted(t) else False
