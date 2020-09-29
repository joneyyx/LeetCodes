# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
#
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap,
# then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
from queue import Queue


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        dfs 方法1，修改了树的结构
        :param t1:
        :param t2:
        :return:
        """
        if not t1:
            return t2
        if not t2:
            return t1

        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        dfs 方法2，不修改树的结构，通过定义一个新的TreeNode
        :param t1:
        :param t2:
        :return:
        """
        if not t1:
            return t2
        if not t2:
            return t1

        newNode = TreeNode(t1.val+t2.val)
        newNode.left = self.mergeTrees(t1.left, t2.left)
        newNode.right = self.mergeTrees(t1.right, t2.right)

        return newNode

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        bfs 方法，queue
        :param t1:
        :param t2:
        :return:
        """
        if not t1:
            return t2
        if not t2:
            return t1

        queue = Queue()
        queue.put(t1)
        queue.put(t2)
        while not queue.empty():
            node1 = queue.get()
            node2 = queue.get()

            node1.val = node1.val + node2.val
            # node1的左子树不存在
            if not node1.left:
                node1.left =  node2.left
            # else表示node1必定存在，所以node2是否为null无关紧要。 并且只有当node2不为null的时候才可以加入的queue，因为queue中的数字都可以进行合并
            elif node2.left:
                queue.put(node1.left)
                queue.put(node2.left)

            if not node1.right:
                node1.right = node2.right
            elif node2.right:
                queue.put(node1.right)
                queue.put(node2.right)
        return t1