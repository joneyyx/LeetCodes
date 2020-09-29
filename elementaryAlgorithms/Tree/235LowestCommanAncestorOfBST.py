# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
# Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
#
# Example 1:
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

class TreeNode():
    def __init__(self, x):
        self.val =  x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        一次遍历，同时找两个节点的路径
        :param root:
        :param p:
        :param q:
        :return:
        """
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        两次遍历，分别找到前往q，p的路径
        :param root:
        :param p:
        :param q:
        :return:
        """

        def getPath(root, target):
            path = []
            while root != target:
                path.append(root)
                # because the prequisist is !=
                if root.val > target.val:
                    root = root.left
                else:
                    root = root.right
            # 加上最后一个点
            path.append(root)

            return path

        path_q = getPath(root, q)
        path_p = getPath(root, p)

        ancestor = None
        for a, b in zip(path_p, path_q):
            if a == b:
                ancestor = a
            else:
                break

        return ancestor
