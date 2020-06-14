# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:
#
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h, n = len(haystack), len(needle)
        if needle == '':
            return 0
        elif h >= n:
            i = 0
            for i in range(h - n + 1):
                substr = haystack[i:i + n]
                h_key = self.calWindow(substr)
                n_key = self.calWindow(needle)
                if h_key == n_key:
                    return i
            return -1
        else:
            return -1

    def calWindow(slf, ipt):
        dictArray = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
                     'm': 12,
                     'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23,
                     'y': 24,
                     'z': 25}
        opt = 0
        for wd in ipt:
            opt = (opt + dictArray.get(wd)) * 26
        return opt


s = Solution()
haystack = ""
needle = "a"
print(s.strStr(haystack, needle))
