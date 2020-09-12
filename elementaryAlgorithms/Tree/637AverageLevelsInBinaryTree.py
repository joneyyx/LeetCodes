# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
from queue import Queue
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        """
        BFS->层序遍历 Queue
        :param root:
        :return:
        """
        if not root:
            return []

        node_list, res= [root], []

        while node_list:
            # children_list to store the children of each row nodes
            # layer_val to store the value of nodes in this row
            children_list, layer_value = [], []
            for cur_node in node_list:
                layer_value.append(cur_node.val)
                if cur_node.left:
                    children_list.append(cur_node.left)
                if cur_node.right:
                    children_list.append(cur_node.right)
            # 每做完一次循环，都会把下一层的node给找出来，存入node_list
            node_list = children_list
            res.append(self.getAverage(layer_value))

        return res

    def getAverage(self, valueList):
        sum = 0
        for item in valueList:
            sum += item
        return sum/len(valueList)

