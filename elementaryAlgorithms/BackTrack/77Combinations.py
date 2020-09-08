# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# You may return the answer in any order.
# Example 1:
#
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# Example 2:
#
# Input: n = 1, k = 1
# Output: [[1]]
#
# Constraints:
#
# 1 <= n <= 20
# 1 <= k <= n
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < k:
            return []

        nums = [i for i in range(1, n+1)]
        res = []

        def back_track(nums_cut, tmp, index):
            if len(tmp) == k:
                res.append(tmp[:])##浅拷贝，这一步很重要
                return
            # 每一次进行平移一个单位的nums
            for i in range(index, n):
                # print(i, index, nums)
                # 1 <= n <= 20
                # 作为append的基础，nums不能剪切
                tmp.append(nums[i])
                # 重点是i+1，这样可以每次都避免做重复的值
                back_track(nums_cut[index:], tmp, i + 1)
                tmp.pop()

        back_track(nums, [], 0)
        return res

s=Solution()
s.combine(3,3)



