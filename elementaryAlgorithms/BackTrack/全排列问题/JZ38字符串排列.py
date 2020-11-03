# 输入一个字符串，打印出该字符串中字符的所有排列
# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素
# 输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        res, path = [], []
        strs = sorted(s)

        isUsed = [0 for i in range(len(strs))]

        def back_track(path, index):
            if index == len(strs):
                res.append("".join(path))
                return

            for i in range(len(strs)):
                if isUsed[i] == 1:
                    continue
                elif i >0  and strs[i] == strs[i-1]  and isUsed[i-1] == 0:
                    continue
                else:
                    path.append(strs[i])
                    isUsed[i] = 1
                    back_track(path, index+1)
                    isUsed[i] = 0
                    path.pop()

        back_track(path, 0)

        return(res)

s=Solution()
res = s.permutation("abb")