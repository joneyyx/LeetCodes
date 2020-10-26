# Given a string s, return the longest palindromic substring in s.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        start_idx = 0
        max_length = 1

        dp = [[False for _ in range(size)] for _ in range(size)]

        for i in range(size):
            dp[i][i] = True

        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                #slice the string
                if dp[i][j] == True:
                    temp_length = j - i +1
                    if max_length < temp_length:
                        max_length = temp_length
                        start_idx =i
        # print(s[start_idx: max_length+start_idx])

        return s[start_idx: max_length+start_idx]

s= Solution()
s.longestPalindrome("abcbad")
