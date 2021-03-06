# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
# 示例:
#
# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    dp[i][j] = grid[i][j]
                elif i  == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j  == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else: dp[i][j] = min(dp[i-1][j], dp[i][j-1]) +grid[i][j]

        return dp[-1][-1]
s=Solution()
grid = [[1,2,5],[3,2,1]]
s.minPathSum(grid)
