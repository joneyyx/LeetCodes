#
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.
#
# Example 1:
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:
#
# Input: "race a car"
# Output: false

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "race a car"
        s1 = ''.join([x for x in s if x.isalpha() or x.isalnum()]).upper()
        if len(s1) < 1:
            return True
        else:
            l, r = 0, len(s1) - 1
            print("L:" + s1[l])
            print("R: " + s1[r])
            while l < r:
                if s1[l] != s1[r]:
                    return False
                    break
                l += 1
                r -= 1
            return True

s = "0P"
S= Solution()
print(S.isPalindrome(str))