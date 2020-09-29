# Given a string s, find the length of the longest substring without repeating characters.
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:
#
# Input: s = ""
# Output: 0

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        max_length = 0

        check_set = set()
        j = 0
        for i in range(len(s)):
            if i != 0:
                check_set.remove(s[i-1])
            # 当发现set中有重复字符时，指针i往右移动一位
            while j < len(s) and s[j] not in check_set:
                check_set.add(s[j])
                j += 1
                print(i, j)

            max_length = max(max_length, j - i)

        return max_length



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j, max_length, dict = 0, 0, {}
        for i, c in enumerate(s):
            # 当循环的字母在字典里出现过之后
            if c in dict:
                j = dict[c]
                dict[c] = i
            else:
                # 字典里没有字母-》将i的坐标给字母
                dict[c] = i
                max_length=max(max_length, i-j)


s= Solution()
s.lengthOfLongestSubstring('pwwkew')

