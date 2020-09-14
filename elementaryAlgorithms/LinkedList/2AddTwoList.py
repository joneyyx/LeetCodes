# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        preNode = cur = ListNode(None)
        # digit has 0/1
        add_val = 0
        #循环条件中有add val是因为要保证，如果99+11， 最后一位是进一点情况下还能继续循环
        while l1 or l2 or add_val:
            # 在对应相加点时候，如果没有这个Node，就赋值0
            add_val =  add_val + (l1.val if l1 else 0) + (l2.val if l2 else  0)
            #最后一个点是 求%
            cur.next = ListNode(add_val % 10)

            cur =  cur.next

            #求进位
            add_val = add_val // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return preNode.next



def generateList(l: list) -> ListNode:
    prenode = ListNode(None)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next

def printList(l: ListNode):
    while l:
        print("%d, " %(l.val), end = '')
        l = l.next
    print('')

if __name__ == "__main__":
    l1 = generateList([1, 5, 8])
    l2 = generateList([9, 1, 2, 9])
    printList(l1)
    printList(l2)
    s = Solution()
    sum = s.addTwoNumbers(l1, l2)
    printList(sum)
