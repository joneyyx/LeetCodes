# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
# Input:
#
# 1
# \
# 3
# /
# 2
#
# Output:
# 1
#
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1( or between 2 and 3).

class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#1递归： 中序遍历得到-->用数组暂存结果，进行排序
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = []

        def dfs(root):
            if not root:
                return


            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)

        mini_val = float('inf')

        for i in range(len(res) - 1):
            mini_val = min(mini_val, res[i + 1] - res[i])

        return mini_val

#2递归：中序遍历得到-->过程中临时值
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # 临时值用负值
        mini_val = float('inf')
        pre = -1

        def dfs(root):
            nonlocal mini_val,pre

            if not root:
                return

            dfs(root.left)

            # 第一个不做
            if pre != -1:
                mini_val = min(mini_val, root.val - pre)
                # 维护更新pre
            pre = root.val

            dfs(root.right)

        dfs(root)
        return mini_val

# 时间复杂度：O(n)，其中 nn 为二叉搜索树节点的个数。每个节点在中序遍历中都会被访问一次且只会被访问一次，因此总时间复杂度为 O(n)。
# 空间复杂度：O(n)。递归函数的空间复杂度取决于递归的栈深度，而栈深度在二叉搜索树为一条链的情况下会达到 O(n) 级别。



#3迭代：中序遍历得到-->过程中临时值

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        stack=[]
        cur = root
        pre,mini_val = -1, float('inf')
        # 中序遍历
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()

            if pre != -1:
                mini_val = min(mini_val, cur.val - pre)
            pre = cur.val

            cur = cur.right
        return mini_val