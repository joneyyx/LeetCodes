# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
#
# 要求时间复杂度为O(n)。
#
#  
#
# 示例1:
#
# 输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        这道题的关键在于"最大连续"
        dp[i]含义为：以nums[i]为结尾的，最大连续子串，
        1 if dp[i-1] > 0 的时候，dp[i]就是它+nums[i]
        2.if dp[i-1] < 0， 对nums[i]造成不好影响，所以还不如nums[i]
        :param nums:
        :return:
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(dp)):
            if dp[i-1] <= 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
        return max(dp)

s=Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
s.maxSubArray(nums)
