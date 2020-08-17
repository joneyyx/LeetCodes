# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Example 1:
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#  
#
# Constraints:
# 1 <= n <= 45
#


# 1. basic 递归思想
#终止条件 n =1 or n = 0
class Solution:
    def climbStairs(self, n: int) -> int:
      if n ==1 or n == 0 :
          return 1
      else:
          return self.climbStairs(n-1)+self.climbStairs(n-2)

# 1.2 递归思想的改进
# 因为有重复的，可以把每一次记录的值存入哈希表，这样就不需要进行额外计算
# 或者用数组，下标为阶梯i
# 时间复杂度和空间复杂度均可以降低为On



# 2. DP
# bottom-up的思想。得到最优子结构

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return (dp[n])

s=Solution()
s.climbStairs(5)

# 维持len=3的数组用来存放pre prepre 和cur节省空间

class Solution:
    def climbStairs(self, n: int) -> int:
        pre = 1
        cur = 1
        for i in range(2, n+1):
            tmp = cur
            cur = pre + tmp
            pre = tmp
        print(cur)



