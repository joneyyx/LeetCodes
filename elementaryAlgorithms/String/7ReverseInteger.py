# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
#Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.123
123 // 10
class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        num = abs(x)
        upper = 2 ** 31 -1
        lower = - 2** 31
        while num >0:
            result = result * 10 + num %10
            if result > upper or result < lower:
                return 0
            num = num //10
        if x > 0:
            return result
        else:
            return  -result