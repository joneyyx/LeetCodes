# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#
#
# Example:
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
from typing import List
# *******首先要定义全局变量存储临时结果以及返回结果（回溯算法相比于递归算法的关键之处）；
# 在递归函数中，首先要判断是否满足递归条件，不满足直接返回；
# 其次，要对当前状态的每一种情况进行循环递归处理；这其中就包含了对临时结果的添加（方便进入下一层递归）以及删除（方便回溯到上一层）操作。
# 注意：正是这样的全局变量保证了回溯操作的正常进行！

# 本质是树的形式，进行一个全局的遍历。
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # 1 exception
        if not digits:
            return []

        dict ={
           '2':['a','b','c'],
           '3': ['e', 'f', 'd'],
           '4': ['g', 'h', 'i'],
           '5': ['j', 'k', 'l'],
           '6': ['m', 'n', 'o'],
           '7': ['p', 'q', 'r', 's'],
           '8': ['t', 'u', 'v'],
           '9': ['w', 'x', 'y', 'z']
               }
        # tmp 用来存取每次做完的结果
        # i作为digitals的index，当递增到4的时候已经算好一条分支
        res = []

        def dfs(tmp, i):
            if i == len(digits):
               res.append(tmp)
            else:
                numberRef = dict[digits[i]]

                for wd in numberRef:
                    dfs(tmp+wd, i+1)

        dfs("", 0)

        return res




s = Solution()
s.letterCombinations('23')