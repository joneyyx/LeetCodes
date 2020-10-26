# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes. Only nodes itself may be changed

# Definition for singly-linked list.


# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Example 2:
#
# Input: head = []
# Output: []
# Example 3:
#
# Input: head = [1]
# Output: [1]


#1  stack
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        1。创建dummy节点，第一个有数字的节点为current。
        2。在运算中用dummy，最后返回的是dummy的复制
        :param head:
        :return:
        """
        #异常检测
        if not (head and head.next):
            return head

        stack = []
        dummy = ListNode(-1)
        p, cur = dummy, head

        while cur and cur.next:
            #将两个节点存入stack
            stack.append(cur)
            stack.append(cur.next)
            #cur位置向后跳一个
            cur = cur.next.next
            #stack出栈
            dummy.next = stack.pop()
            dummy.next.next = stack.pop()
            #这一步很关键，dummy又一次移动到现在的cur前面
            dummy =  dummy.next.next

        #最后剩下1个或者没有
        if cur:
            dummy.next = cur
        else:
            dummy.next = None

        return p.next

#2 recrusive

class Solution(object):
	def swapPairs(self, head):
		# 递归的终止条件
		if not (head and head.next):
			return head
		# 假设链表是 1->2->3->4
		# 这句就先保存节点2
		tmp = head.next
		# 继续递归，处理节点3->4
		# 当递归结束返回后，就变成了4->3
		# 于是head节点就指向了4，变成1->4->3
		head.next = self.swapPairs(tmp.next)
		# 将2节点指向1
		tmp.next = head
		return tmp

