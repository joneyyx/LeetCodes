# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.
#
#  
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
# Example 2:
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.
from typing import List

# 此题重点是不光要写出转移方程dp[i] = dp[i-2] +nums[i]
# 还要与前一个dp[i-1】进行比较，因为题目要求不相邻，所以可能隔两位
# 对于连续的 nn 栋房子：H~1~,H~2~,H~3~......H~n~H 1 ,H 2 ,H 3 ......H n ，小偷挑选要偷的房子，且不能偷相邻的两栋房子，方案无非两种：
# 方案一：挑选的房子中包含最后一栋；
# 方案二：挑选的房子中不包含最后一栋；
# 获得的最大收益的最终方案，一定在这两种方案中产生，用代码表述就是：
# 最优结果 = Math.max(方案一最优结果，方案二最优结果)

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 ] *n
        # 边界时长度为0
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in  range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        maxRob = dp[0]
        for i in range(1, n):
            maxRob = max(maxRob, dp[i])
        return (maxRob)
s= Solution()
s.rob([1,5,2,1,3])