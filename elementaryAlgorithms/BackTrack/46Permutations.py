# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        # res to store the final features:
        res = []
        # track to store the values
        n = len(nums)
        def back_track(tmp, index):
            if index == n:
                res.append(tmp[:])
                return
            for i in range(n):
                if nums[i] in tmp:
                    continue
                tmp.append(nums[i])
                back_track(tmp, index+1)
                tmp.pop()

        back_track([], 0)
        return res

s=Solution()
s.permute([1,2,3])



# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         def backtrack(nums, tmp):
#             if not nums:
#                 res.append(tmp)
#                 return
#             for i in range(len(nums)):
#                 backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
#         backtrack(nums, [])
#         return res