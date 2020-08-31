# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
# Example:
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
from typing import List

# 数组问题，可以用双指针解决
# 1。一开始的思路是通过慢慢缩小X轴的变长来进行操作。 数组长度位8，变长位7。   如果缩小长度为7，那么就有两个变长为6。
# 2。 后面发现，每次去掉首位长度较短的一边就可以操作了
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # i and j equals to the first and last number
        i, j = 0 ,len(height)-1
        max_area = 0

        if len(height) == 1:
            return max_area

        while i < j:
            if height[i] <= height[j]:
                max_area = max(max_area, height[i] * (j-i))
                i += 1
            else:
                max_area = max(max_area, height[j] * (j-i))
                j -=1
        return max_area
s =Solution()
s.maxArea([1,8,6,2,5,4,8,3,7])
