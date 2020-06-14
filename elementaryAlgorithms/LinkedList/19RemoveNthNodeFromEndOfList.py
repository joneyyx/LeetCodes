# Given a linked list, remove the n-th node from the end of list and return its head.
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        preNode = ListNode(None)
        preNode.next = head
#         定义指针first, second=> 指针在这里可以用哨兵节点preNode来代替
        first, second = preNode, preNode
        for i in range(n):
            first = first.next
        # 当指针的下一个节点是None，就可以停止运算
        while first.next != None:
            first = first.next
            second = second.next
#         现在second是的节点就是需要删除的
        second.next = second.next.next
        return preNode.next

