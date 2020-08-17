# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
from typing import List
# 通常我们遍历子串或者子序列有三种遍历方式
#
# 1.以某个节点为开头的所有子序列: 如 [a]，[a, b]，[ a, b, c] ... 再从以 b 为开头的子序列开始遍历 [b] [b, c]。
# 2.根据子序列的长度为标杆，如先遍历出子序列长度为 1 的子序列，在遍历出长度为 2 的 等等。
# 3.以子序列的结束节点为基准，先遍历出以某个节点为结束的所有子序列，因为每个节点都可能会是子序列的结束节点，因此要遍历下整个序列，如:
# 以 b 为结束点的所有子序列: [a , b] [b] 以 c 为结束点的所有子序列: [a, b, c] [b, c] [ c ]。
# 第一种遍历方式通常用于暴力解法, 第二种遍历方式 leetcode (5. 最长回文子串 ) 中的解法就用到了。
#
# 第三种遍历方式 因为可以产生递推关系, 采用动态规
# 对于刚接触动态规划的, 我感觉划时, 经常通过此种遍历方式, 如 背包问题, 最大公共子串 , 这里的动态规划解法也是以 先遍历出 以某个节点为结束节点的所有子序列 的思路
# #熟悉第三种遍历方式是需要抓住的核心

#思路
# 1. 以结尾为基准，写出所有子序列。
# ~~定义dp[i]的含义： 以index i为节点为结束点的时候，前面子序列的最大值
# 比如dp[2], 当index i =2 时，即结束点=3的时候，前面子序列的最大值为dp[2]
#
# 2. 举例并找出状态转移方程
# dp[1] : [-2, 1], [1]
# dp[2] : [-2, 1, -3], [1, -3], [-3]
#
# *****dp[i] = Max(dp[i-1] + nums[i], nums[i])
# *****if dp[i-1] > = 0: 则dp[i] = dp[i-1] + nums[i]
# *****else:  dp[i] = nums[i-1]
# 因为如果前一个的子序列为负，则不管加nums为正负都会比nums本身小。
#
# 3. 初始化
# dp[0] = nums[0]
# 对于第一个dp来说他的最大值就一个
#
#
# 4. 状态压缩，优化数组空间====


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [0 for i in range(n)]
#         initialization
        dp[0] = nums[0]

        # 注意从index = 1开始
        # for i in range(1, n):
        #     if dp[i-1] >= 0:
        #         dp[i] = dp[i-1] + nums[i]
        #     else:
        #         dp[i] = nums[i]

        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i],   nums[i])
        #也可以通过比较最大值来进行，但效率没有上述的高

#         find the biggest
        biggest = dp[0]
        for i in range(1, n):
            biggest = max(biggest, dp[i])
        return (biggest)

s = Solution()
s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])


# 优化
# 因为dp[i]只与dp[i-1]有关，所以我们只需要留两个变量，一个是全局最大Totalbig,还有一个是前一个最大:SubBig
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        totalBig = nums[0]
        subBig = nums[0]

        n = len(nums)
        if nums == None:
            return 0

        for i in  range(1, n):
            if subBig >= 0:
                subBig = subBig + nums[i]
            else:
                subBig = nums[i]
            totalBig = max(totalBig, subBig)
        return totalBig



#         find the biggest



