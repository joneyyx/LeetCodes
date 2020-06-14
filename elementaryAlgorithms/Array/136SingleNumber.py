# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4
from typing import List

# method 1:

# 因为是只有一个数唯一，其余的数都是重复，
# 先取set，然后*2
# 再减去原来的
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         nbr = 2*sum(set(nums))-sum(nums)
#         return nbr

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = 0
        for i in range(len(nums)):
            d = d ^ nums[i]
        return d

nums = [4,1,2,1,2]
s=Solution()
print(s.singleNumber(nums))


