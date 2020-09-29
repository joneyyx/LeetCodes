# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
from typing import List


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Solution1 : Back_track
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], [] if not root else [root.val]

        def back_track(path, root, count):
            # 递归的终止条件要同时满足：1 是叶子节点（左右都没有值）， 2 count=0
            if (count == 0) and (not root.left) and (not root.right):
                res.append(path[:])

            # 对let和right分别进行回溯
            if root.left:
                count -= root.left.val
                path.append(root.left.val)
                back_track(path, root.left, count)
                count += root.left.val
                path.pop()

            if root.right:
                count -= root.right.val
                path.append(root.right.val)
                back_track(path, root.right, count)
                count += root.right.val
                path.pop()

        # main
        if not root:
            return []
        else:
            back_track(path, root, sum - root.val)
        return res


#Solution2 Recrusion
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        """
        对于递归解法
        :param root:
        :param sum:
        :return:
        """
        res , path= [], [] if not root else [root.val]
        def check_dfs(path, root, count):
            if not root:
                return []
            path.append(root.val)
            count -= root.val
            if not root.left and not root.right and count == 0:
                res.append(path[:])
            check_dfs(path, root.left, count)
            check_dfs(path, root.right, count)
            path.pop()

        check_dfs(path, root, sum)