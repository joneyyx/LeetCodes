# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
#
#  
#
# 示例 1:
#
# 输入: 12258
# 输出: 5
# 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"


class Solution:
    def translateNum(self, num: int) -> int:

        strNum = str(num)
        #"dp有0，意味着没有选择的情况。 dp1=字符第一位的情况"
        dp = [ 1 for _ in range(len(strNum)+1)]
        for i in range(2,len(strNum)+1):
            if strNum[i-2] == '1' or (strNum[i-2] == '2' and strNum[i-1] < '6'):
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
            print(i, dp[i])
        return dp[len(strNum)]

s=Solution()
print(s.translateNum(631))

