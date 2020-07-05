# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        # final result
        res = []

        from collections import deque
        que = deque()
        que.append(root)
        # equals que is not None
        while que:
            temp = []
            # 第一层一个node，所以做一次循环。 第二层两次node，做两次循环。
            # 每一次循环都分别从que里面取出第一个元素。
            que_length = len(que)
            for i in range(que_length):
                node = que.popleft()
                # 把这一层的节点的值存起来
                temp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            # 每一层的node作为一个list存入result中
            res.append(temp)
        return res



