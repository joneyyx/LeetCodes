# Given the root of a binary tree, return the postorder traversal of its nodes' values.
#
# Input: root = [1,null,2,3]
# Output: [3,2,1]
#
# Input: root = []
# Output: []
#
# Input: root = [1]
# Output: [1]
#
# Input: root = [1,2]
# Output: [2,1]
#
# Input: root = [1,null,2]
# Output: [2,1]
from typing import List


class TreeNode():
    def __init__(self, val = 0 , left =None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        #递归
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            dfs(root.left)
            res.append(root.val)
            return res

        return dfs(root)



class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        cur = root
        # 后序遍历找右下角并且最后结果相反
        # 前序遍历找左下角
        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur =  cur.right
            cur = stack.pop()
            cur = cur.left
        return res[::-1]

