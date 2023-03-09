# Definition for singly-linked list.

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        node_list = []
        n = 0
        while head:
            node_list.append(head)
            n += 1
            head = head.next

        return node_list[n // 2]




