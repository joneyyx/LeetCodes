# Definition for a binary tree node.
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,3,2]
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归
# 时间复杂度：O(n)，n为节点数，访问每个节点恰好一次。
# 空间复杂度：空间复杂度：O(h)，h为树的高度。最坏情况下需要空间O(n)，平均情况为O(logn)



# 递归1
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        inorder => left-node-right
        :param root:
        :return:
        """
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

# 递归2
# 递归2：通用模板，可以适应不同的题目，添加参数、增加返回条件、修改进入递归条件、自定义返回值
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        inorder => left-node-right
        :param root:
        :return:
        """
        res = []

        def dfs_rec(node):
            if not node:
                return None
            # 中序递归
            dfs_rec(node.left)
            res.append(node.val)
            dfs_rec(node.right)

            # #前序递归
            # res.append(node.val)
            # dfs_rec(node.left)
            # dfs_rec(node.right)
            # #后序递归
            # dfs_rec(node.left)
            # dfs_rec(node.right)
            # res.append(node.val)

        dfs_rec(root)
        return res
