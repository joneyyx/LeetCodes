# 58. Length of Last Word
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a maximal substring consisting of non-space characters only.
#
# Example:
#
# Input: "Hello World"
# Output: 5

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        n = len(s)-1
        while n >= 0:
            flag = False
            while n >= 0 and  s[n] != " ":
                flag = True
                length += 1
                n -= 1
            # 没有遇到不为" "的就继续做
            n -= 1
            if  flag:
                break
        return length
s=Solution()
s.lengthOfLastWord("Hello World ")



