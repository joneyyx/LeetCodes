# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Example 2:
#
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []

        def back_track(path, number, k, index):
            if number == 0 and k==0:
                res.append(path[:])
                return
            # 求组合问题，无序->所以需要起点index
            for i in range (index, 10): #添加的数字就是1-9， index作为开头，保证了相同循环里面后面的数字增大
                if i > number:
                    continue
                path.append(i)
                # 下面的i+1对应index，index每次要多加1避免重复输入
                back_track(path, number-i, k-1,  i+1 )
                path.pop()
        back_track([], n, k, 1)
        return res

s=Solution()
s.combinationSum3(3,9)
