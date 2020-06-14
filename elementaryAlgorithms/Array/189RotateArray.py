# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Example 1:
#
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:
#
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# Note:
#
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?
# from typing import List
# 三次反转
# 对于[1,2,3,4,5,6,7][1,2,3,4,5,6,7]，
# 根据k=k\%nk=k%n，将数组分为两段：
#
# 第一段，对应数组下标范围[0,n-k-1][0,n−k−1]段，即[1,2,3,4][1,2,3,4]
# 第二段，对应数组下标范围[n-k,n-1][n−k,n−1]，即[5,6,7][5,6,7]
# 分为三步：
#
# 反转第一段，[4,3,2,1,5,6,7]
# 反转第二段，[4,3,2,1,7,6,5]
# 反转整体，[5,6,7,1,2,3,4]
# 完成！
#
# 复杂度分析
# 时间复杂度：O\left(n\right)O(n)
# 空间复杂度：O(1)O(1)
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # key代表了数组有多少个被移动到最前
        n = len(nums)
        k = k%n
        def swap(p, q):
            while(p < q):
                nums[p], nums[q]= nums[q],nums[p]
                p += 1
                q -= 1
        swap(0, n-k-1)
        swap(n-k, n-1)
        swap(0, n-1)
        return nums


s = Solution()
print(s.rotate([1,2,3,4,5], 3))

nums=[1,2,3,4,5]
nums[-2:]