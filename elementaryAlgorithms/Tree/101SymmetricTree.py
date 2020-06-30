# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#  
#
# But the following [1,2,2,null,3,null,3] is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#  
#
# Follow up: Solve it both recursively and iteratively.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 方法1： 中序遍历之后验证是否是回文

# 方法2： 递归
# 终止条件：root is None
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        # 调用
        return self.helper(root.left, root.right)


    def helper(self, left, right):
        # equal to : if left is None and right is None
        # (left or right) = > left =1 or right =1   =>至少有一个
        # not (left or right) =>  left =0 and right = 0  =>一个都没有
        if not (left or right):
            return True
        # equal to : if left is None   or right is None
        # (left and right) = > left =1 and right =1   =>两个都有
        # not (left and right) =>  left =0 or right = 0  =>有一个节点没有
        if not (left and right):
            return False
        if left.val != right.val:
            return False

#         前三部下来，保证了第一个left和right即是存在的，也是对称的
        return (self.helper(left.left, right.right) and self.helper(left.right, right.left))

# 递归版本代码2
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        # 调用
        def helper(left, right):
            # equal to : if left is None and right is None
            # (left or right) = > left =1 or right =1   =>至少有一个
            # not (left or right) =>  left =0 and right = 0  =>一个都没有
            if not (left or right):
                return True
            # equal to : if left is None   or right is None
            # (left and right) = > left =1 and right =1   =>两个都有
            # not (left and right) =>  left =0 or right = 0  =>有一个节点没有
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            #         前三部下来，保证了第一个left和right即是存在的，也是对称的
            return (helper(left.left, right.right) and helper(left.right, right.left))

        return helper(root.left, root.right)


#迭代，使用队列

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue= [root.left, root.right]
        while queue:
            # left , right 分别为队列的前两个元素
            left = queue.pop(0)
            right = queue.pop(0)
            # 迭代和递归的差别在这里*********
            # 因为我们的结束条件是知道queue is None，所以我们当两者都为null的时候，就继续进行操作。因为此时他们是两个Null节点。
            if not (left or right):
                continue
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            # 成对添加
            queue.append(left.left)
            queue.append(right.right)

            queue.append(left.right)
            queue.append(right.left)

        # 元素全部结束没有报错的话，就是True
        return True
