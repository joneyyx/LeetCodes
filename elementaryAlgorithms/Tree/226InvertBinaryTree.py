# 翻转一个二叉树
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(cur):
            if not cur:
                return
            cur.left = dfs(cur.right)
            cur.right = dfs(cur.left)

        dfs(root)
        return root