# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        t = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                t = True
                break
        
        if not t:
            return None
        curr = head
        while curr != slow:
            curr = curr.next
            slow = slow.next
        return slow
