# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
#
# Input: [3,2,3]
# Output: 3
# Example 2:
#
# Input: [2,2,1,1,1,2,2]
# Output: 2
#1. 计算个数法
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for i, c in enumerate(nums):
            dict[c] = dict.get(c, 0) + 1
        for key in dict.keys():
            if dict[key] > len(nums)/2:
                return key


#2.排序
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # dict = {}
        # for i, c in enumerate(nums):
        #     dict[c] = dict.get(c, 0) + 1
        # for key in dict.keys():
        #     if dict[key] > len(nums)/2:
        #         return keydef merge(left, right):
        def merge(left, right):
            res = []
            p, q = 0, 0
            # 当list是>1
            while p < len(left) and q < len(right):
                if left[p] < right[q]:
                    res.append(left[p])
                    p += 1
                else:
                    res.append(right[q])
                    q += 1
            # 当左右两个排序后的数组，左边排序完了，右边的直接入站
            if p == len(left):
                while q < len(right):
                    res.append(right[q])
                    q += 1
            else:
                while p < len(left):
                    res.append(left[p])
                    p += 1
            return res

        def merge_sort(lists):
            if len(lists) <= 1:
                return lists
            middle = len(lists) // 2
            left = merge_sort(lists[:middle])
            right = merge_sort(lists[middle:])
            return merge(left, right)

        res = merge_sort(nums)
        return res[len(nums) // 2]

s=Solution()
s.majorityElement([2,2,1,1,1,2,2])