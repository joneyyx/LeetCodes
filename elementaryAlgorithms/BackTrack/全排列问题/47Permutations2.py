# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
# Example 1:
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

# Example 2:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        #对nums排序，相同的放在一起
        nums.sort()
        #建立一个数组， isUsed， 对应长度为nums， 0代表这一位上的nums没有用过，1代表这一位上的nums用过
        isUsed = [0 for i in range(len(nums))]
        def back_track(path, index):
            if index ==  len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                #每一层循环因为都要重新开始遍历数组， isUsed=1表示上一层已经使用过，直接跳过
                if isUsed[i] == 1:
                    continue
                #数字相等，但是nums[i-1]==0的情况下，说明i开辟了新的分支。且分支的开头元素和i-1开辟的一样。
                #这样就会导致后序重复
                if i > 0 and (nums[i-1] == nums[i]) and (isUsed[i-1] == 0):
                    continue
                else:
                    path.append(nums[i])
                    isUsed[i] = 1
                    back_track(path, index+1)
                    path.pop()
                    isUsed[i] = 0

        back_track(path, 0)
        return res

s = Solution()
s.permuteUnique([1,1,2])