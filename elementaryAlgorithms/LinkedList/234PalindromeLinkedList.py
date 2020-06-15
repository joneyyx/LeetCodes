# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
# Example 2:
#
# Input: 1->2->2->1
# Output: true


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        pre = None
        if not head or not head.next:
            return True
        else:
            slow = head
            fast = head.next

        while fast and fast.next:
            tmp = slow
            slow = slow.next
            fast = fast.next.next
            tmp.next = pre
            pre = tmp

        # 此处是精髓：奇偶情况下分别拆成两个链表
        if fast:
            fast = slow.next
            slow.next = pre
        else:
            fast =  slow.next
            slow = pre

        # compare
        while fast and slow:
            if fast.val != slow.val:
                return False
            else:
                fast = fast.next
                slow = slow.next

        return  True