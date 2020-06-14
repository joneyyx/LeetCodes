# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashDict={}
# hash表记录的是位数
        for id, nb in enumerate(nums):
            hashDict[nb] = id
        for i, nb2 in enumerate(nums):
            c = target - nb2
            j = hashDict.get(c)
#            i,j 不应一样
            if i != j and j is not None:
                return [i,j]



s=Solution()
s.twoSum([2,4,11,5],6)