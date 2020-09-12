# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates =[10,1,2,7,6,1,5], target =8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example 2:
#
# Input: candidates =[2,5,2,1,2], target =5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return

        res = []

        def back_track(nums, temp, number, start):
            if number  == 0:
                res.append(temp[:])
                return
            # start是为了减少复杂度
            for i in range(start, len(nums)):
                # avoid 避免同一行里面出相同元素
                if i > start and nums[i-1] == nums[i]:
                    continue
                if nums[i] > number:
                    continue
                temp.append(nums[i])
                # i+1 避免list里面的数字重复使用
                back_track(nums, temp, number-nums[i], i+1)
                temp.pop()

        # 排序之后避免一层使用相同的元素
        candidates.sort()
        back_track(candidates, [], target, 0)
        return res

s=Solution()
s.combinationSum2([10,1,2,7,6,1,5], 8)



class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if (not candidates) or (len(candidates) == 0):
            return []
        path = []
        res = []
        candidates.sort()
        self.__DFS(candidates, target, 0, path, res)
        return res


    def __back_track(self, candidates, target, begin, path, res):
        path = path.copy()
        if target == 0:
            res.append(path)
            return

        if begin > len(candidates) -1:
            return

        #track_back
        for cur in range(begin, len(candidates)):
            if cur > begin and candidates[cur - 1] == candidates[cur]:  # 数组常见去重复的方法，对于重复的数值，我们只让第一个进入循环，后面的就不要再进入循环了
                continue

            temp = target - candidates[cur]

            # cut
            if temp < 0:
                return
            else:
                path.append(candidates[cur])
                self.__back_track(candidates, temp, cur+1, path, res)
                path.pop()
