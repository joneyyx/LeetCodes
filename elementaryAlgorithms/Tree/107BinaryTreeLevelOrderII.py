# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
        这里用到了BFS，这里用的是while循环的方式来处理队列
        还可以用Queue
        :param root:
        :return:
        """
        if not root:
            # 看清题意返回的是List，不要想当然的None
            return []
        nodeList , res = [root], []
        while nodeList:
            # create a temp list for the nodes in each layer
            # create a temp list to store the node values in each layer
            layer, layerVal = [], []
            for node in nodeList:
                layerVal.append(node.val)
                if node.left: layer.append(node.left)
                if node.right: layer.append(node.right)
            nodeList = layer
            res.append(layerVal)
        return res[::-1]

from queue import Queue
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
        这里用到了BFS，也用到了Queue。
        每一次可以记录一层有几个，循环跑抽取queue中的数
        :param root:
        :return:
        """
        if not root:
            # 看清题意返回的是List，不要想当然的None
            return []
        queue = Queue()
        queue.put(root)
        res =  []

        while not queue.empty():
            size = queue.qsize()
            nodeValue = []

            for _ in range(size):
                node = queue.get()
                nodeValue.append(node.val)
                if node.left: queue.put(node.left)
                if node.right: queue.put(node.right)
            res.append(nodeValue)
        return res[::-1]