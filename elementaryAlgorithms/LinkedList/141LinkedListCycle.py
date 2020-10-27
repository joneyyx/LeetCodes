# Given a linked list, determine if it has a cycle in it.
#
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
#
# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
#
#
# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
#
#
# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
# Follow up:
# Can you solve it using O(1) (i.e. constant) memory?
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#         快慢指针，时间ON， 空间O1，
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        else:
            slow = head
            fast = head

        while fast and slow:
            slow = slow.next
            if fast.next:
                # 只有当fast.next存在的情况下可以存在next.next
                fast = fast.next.next
            else:
                return False
            if slow == fast:
                return  True
        return False


###########################
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dic = {}
        node = head
        while (node):
            if (dic.get(node, 0) != 0):
                return True
            else:
                dic[node] = 1
            node = node.next
        return False
