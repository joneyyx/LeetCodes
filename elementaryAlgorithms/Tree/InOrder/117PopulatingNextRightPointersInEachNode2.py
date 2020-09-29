# Given a Binary Tree
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#

# Follow up:
#
# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
from queue import Queue


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        nodeList=  []

        while nodeList:
            layer = []
            for node in nodeList:
                if node.left: layer.append(node.left)
                if node.right: layer.append(node.right)

              #最后一个不需要进行next，因为默认都是None
            if len(layer) > 1:
                for i in range(len(layer)-1):
                    layer[i].next = layer[i+1]
            nodeList = layer
        return root


