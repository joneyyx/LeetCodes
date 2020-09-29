# Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
#
# Example:
#
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13
#
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13
from typing import List


class TreeNode():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        inorder to list
        :param root:
        :return:
        """
        def dfs(root):
            nonlocal res
            if not root:
                return None
            dfs(root.right)
            res += root.val
            root.val = res
            dfs(root.left)

        res = 0
        dfs(root)
        return root


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        stack (1, root)
        :param root:
        :return:
        """
        stack = [(1,root)]
        sum_val = 0
        while stack:
            color, cur_node = stack.pop()
            if not cur_node:
                continue
            if color == 1:
                stack.append((1, cur_node.left))
                stack.append((0, cur_node))
                stack.append((1, cur_node.right))
            else:
                sum_val += cur_node.val
                cur_node.val = sum_val
        return root


