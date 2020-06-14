# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Note:
#
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
#
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?




# 方法一：hashmap，对较小的构建hashmap。对大的表进行循环
# from typing import List
#
#
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#
#         l1 = len(nums1)
#         l2 = len(nums2)
#
#         if l2 <= l1:
#             return self.intersect(nums2, nums1)
#
#         # 构建较短数组的
#         hashDict = {}
#         for num1 in nums1:
#             hashDict[num1] = hashDict.get(num1,0) + 1
#
#         resultList = []
#         for w in nums2:
#             if w in hashDict and hashDict[w] >0:
#                 resultList.append(w)
#                 hashDict[w] = hashDict.get(w) - 1
#         return resultList




# 对于排序的两个表，分别为他们创建指针i，j。 同时移动，谁小就往后面移动。
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i , j = 0 , 0
        resultList = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] == nums2[j]:
                resultList.append(nums1[i])
                i += 1
                j += 1
            else:
                j += 1
        return resultList



nums1 = [1,2]
nums2 = [2,3,4,3,2]
s = Solution()
result = s.intersect(nums1, nums2)
print(result)




