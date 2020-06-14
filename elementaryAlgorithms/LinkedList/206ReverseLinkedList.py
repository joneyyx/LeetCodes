# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you implement both?


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



# Solution 1: iteratively
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         cur = head
#         pre = None
#         while cur != None:
#             tmp = cur.next
#             cur.next = pre
#             pre = cur
#             cur = tmp
#         return pre


# Solution 2: recursion
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newNode = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newNode

