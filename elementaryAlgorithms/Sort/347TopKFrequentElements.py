# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
# Note:
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
# You can return the answer in any order.
import collections
from typing import List


# 1.遍历nums建立（数字：频次）字典 O（n）
# 2.将字典转为二维列表
# 3.取前K个元素建立大小为K的最小堆O（k）
# 4.剩余k+1到N个个元素依次和堆顶比较，如果比堆顶大，则替换当前堆顶，并维护最小堆 每次调整花费O（logk），最坏的情况O((n-k)logk)
# 5.最终最小堆里就是前K频次高的元素

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        # 1.遍历nums建立（数字：频次）字典 O（n）
        # 2.将字典转为二维列表
        # 3.取前K个元素建立大小为K的最小堆O（k）
        # 4.剩余k+1到N个个元素依次和堆顶比较，如果比堆顶大，则替换当前堆顶，并维护最小堆 每次调整花费O（logk），最坏的情况O((n-k)logk)
        # 5.最终最小堆里就是前K频次高的元素
        :param nums:
        :param k:
        :return:
        """

        # 最小堆维护，shift_down
        def shift(i, k):  # 维护最小堆
            while True:
                t = 2 * i + 1
                if t >= k:
                    return
                if t + 1 < k and hashList[t][1] > hashList[t + 1][1]:
                    t = t + 1
                if hashList[t][1] < hashList[i][1]:
                    hashList[t], hashList[i] = hashList[i], hashList[t]
                    i = t
                else:
                    return

        hashMap = {}
        # for elem in nums:
        #     if elem in hashMap:
        #         hashMap[elem] = hashMap[elem] + 1
        #     else:
        #         hashMap[elem] = 1
        for elem in nums:
            hashMap[elem] = hashMap.get(elem, 0 ) + 1
        # hashMap = collections.Counter(nums)
        # stat = list(hashMap.items())

        # hashMap转化为二维列表
        hashList = [[k,v] for k, v in hashMap.items()]

        # 建立K个元素的最小堆
        for i in range(k, -1, -1):
            shift(i, k)

        for i in range(k, len(hashList)):
            if hashList[i][1] >= hashList[0][1]:
                hashList[0] = hashList[i]
                shift(0, k)
        return [hashList[i][0] for i in range(k)]

s=Solution()
s.topKFrequent([1,1,1,3,3,2,2,2,2,],2)
