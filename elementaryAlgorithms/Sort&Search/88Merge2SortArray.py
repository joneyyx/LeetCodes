# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
# Example:
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6] 
#
# Constraints:
#
# -10^9 <= nums1[i], nums2[i] <= 10^9
# nums1.length == m + n
# nums2.length == n
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # nums1中最后一个元素的位置
        i = m-1
        print("i:", i)
        # nums2中最后一个元素的位置
        j = n-1
        print("j:", j)
        # 目标存放数组，暂时为nums1，中最后一个坑的index
        holder = m+n-1
        print("holder", holder)

        while j >=0 or i >=0:
            if j < 0:
                nums1[holder] = nums1[i]
                i -= 1
            elif i < 0 :
                nums1[holder] = nums2[j]
                j -= 1
            elif nums2[j] >= nums1[i]:
                nums1[holder] = nums2[j]
                j -= 1
            else:
                nums1[holder] = nums1[i]
                i -= 1
            # holder 放在外面更好
            holder -= 1

        print(nums1)

s = Solution()
s.merge([2,0],1,[1],1)

