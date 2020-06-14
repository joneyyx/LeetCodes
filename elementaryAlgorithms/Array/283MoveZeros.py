# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 1
        while j < len(nums):
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
            if nums[i] != 0:
                i += 1
            j += 1
        print(nums)



# 一次遍历
# 这里参考了快速排序的思想，快速排序首先要确定一个待分割的元素做中间点x，然后把所有小于等于x的元素放到x的左边，大于x的元素放到其右边。
# 这里我们可以用0当做这个中间点，把不等于0(注意题目没说不能有负数)的放到中间点的左边，等于0的放到其右边。
# 这的中间点就是0本身，所以实现起来比快速排序简单很多，我们使用两个指针i和j，只要nums[i]!=0，我们就交换nums[i]和nums[j]
# 请对照动态图来理解：
#
# 时间复杂度:O(n)
# 空间复杂度:O(1)
# 代码实现:
#
# javapython
# class Solution(object):
# 	def moveZeroes(self, nums):
# 		"""
# 		:type nums: List[int]
# 		:rtype: None Do not return anything, modify nums in-place instead.
# 		"""
# 		if not nums:
# 			return 0
# 		# 两个指针i和j
# 		j = 0
# 		for i in xrange(len(nums)):
# 			# 当前元素!=0，就把其交换到左边，等于0的交换到右边
# 			if nums[i]:
# 				nums[j],nums[i] = nums[i],nums[j]
# 				j += 1


s = Solution()
s.moveZeroes([0,1,0,3,12])