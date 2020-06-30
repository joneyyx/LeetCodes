# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
# Example 1:
#
#     2
#    / \
#   1   3
#
# Input: [2,1,3]
# Output: true
# Example 2:
#
#     5
#    / \
#   1   4
#      / \
#     3   6
#
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Definition for a binary tree node?
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 方法1， 递归把树，通过中序遍历存入数组，再对数组进行比较。 因为如果是正确的二分查找树的话，通过中序遍历可以得到的一个“不重复”且“递增”的数组

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        def inOrder(root: TreeNode):
            # equal to => is not None
            if root:
                inOrder(root.left)
                stack.append(root)
                inOrder(root.right)

        inOrder(root)

        if root is None:
            return True
        for i in range(len(stack)-1):
           if stack[i].val >= stack[i+1].val:
                return   False
        return True



# 方法2， 对于上面代码的优化
# 因为利用了中序遍历，元素递增的原则，此解可以分两步优化：
# # 1、list是升序的，所以可以每次做add的时候就跟前一个元素做比较，如果curVal<=prevVal，直接return false，这样省去一次list遍历，对于错误情况甚至都不用遍历完BST树；
# # 2、list是升序的，所以当前插入值必定大于前一个元素，即curVal>prevVal必然成立，所以根本不用定义list，只要记录前一个数字即可，这样空间复杂度为O(1)。
# noinspection PyUnresolvedReferences,PyUnusedLocal
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.pre = float('-inf')

        def inOrder(root : TreeNode):
            if not root:
                return True
            if not inOrder(root.left):
                return False
            if self.pre >= root.val:
                return False
            self.pre = root.val
            return inOrder(root.right)
        return inOrder(root)


# 方法3，递归思想
# 那么根据二叉搜索树的性质，在递归调用左子树时，我们需要把上界 upper 改为 root.val，即调用 helper(root.left, lower, root.val)，
# 因为左子树里所有节点的值均小于它的根节点的值。同理递归调用右子树时，我们需要把下界 lower 改为 root.val，即调用 helper(root.right, root.val, upper)。
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        high=float('inf')
        low=float('-inf')
        def inOrder(root: TreeNode, high, low):
            if not root:
                return True
            if root.val <= low or root.val >= high:
                return False
            # left leaf 's high should inherit it's parent
            if not inOrder(root.left, root.val, low):
                return False
            # right leaf
            if not inOrder(root.right, high, root.val):
                return False
            return True
        return inOrder(root, high, low)

