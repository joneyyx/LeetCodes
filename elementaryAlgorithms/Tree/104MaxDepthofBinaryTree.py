#
# Note: A leaf is a node
# with no children.
#
# Example:
# Given binary tree[3, 9, 20, null, null, 15, 7],
#
# 3
# / \
#     9
# 20
# / \
#     15
# 7
# return its
# depth = 3.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 1. DFS
# 再来分析下递归的两个条件：
#
# 1递归终止条件：当节点为空时返回
# 2再次递归计算 max( 左节点最大高度，右节点最大高度)+1

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) +1


# stack
# dfs
# pop
# 右边的孩子先出，所以不能保证最后一个出去的就是最大深度，要用max
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        stack = []
        stack.append((root, 1))
        # equal to => while stack != []:
        depth = 0
        while stack:
            root, cur_depth = stack.pop()
            if root is not None:
                depth = max(depth, cur_depth)
                stack.append((root.left, cur_depth+1))
                stack.append((root.right, cur_depth+1))
        return depth


# queue
# bfs
# pop(0)
# 每次先排出位于第一位的，这样做到最后了之后，结点肯定是位于最下面的。无需比较max
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        stack = []
        stack.append((root, 1))
        # equal to => while stack != []:
        depth = 0
        while stack:
            root, cur_depth = stack.pop()
            if root is not None:
                depth = max(depth, cur_depth)
                stack.append((root.left, cur_depth+1))
                stack.append((root.right, cur_depth+1))
        return depth