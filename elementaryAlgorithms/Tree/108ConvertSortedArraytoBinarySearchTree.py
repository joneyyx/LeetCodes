# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example:
#
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def inOrder(left, right):
            if left > right:
                return None

            # left + (right-left)//2
            mid = (right+left) //2
            node = TreeNode(nums[mid])
            node.left = inOrder(left, mid-1)
            node.right =  inOrder(mid+1 , right)
            return node

        # 初始化的left和right分别是数组的起点和终点
        return inOrder(0, len(nums)-1)