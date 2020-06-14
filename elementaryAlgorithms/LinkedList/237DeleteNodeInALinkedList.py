#
# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
#
# Given linked list -- head = [4,5,1,9], which looks like following:
# Example 1:
#
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
# Example 2:
#
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
#
# Note:
#
# The linked list will have at least two elements.
# All of the nodes' values will be unique.
# The given node will not be the tail and it will always be a valid node of the linked list.
# Do not return anything from your function.


# 只知道要删除的节点。
# 为了删除它，我们必须知道它的上一个节点。但是根据链表的特性，我们对于每一个节点只能知道它的下一个节点的地址。
# 所以我们就把本节点的值用下一个节点的值替代。这样我们删除了下一个节点之后就能保证删除的数字是本节点被替换的数。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
