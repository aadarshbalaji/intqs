# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new = None
        curr = head
        while curr:
            nextnode = curr.next
            curr.next = new
            new = curr
            curr = nextnode
        return new


        