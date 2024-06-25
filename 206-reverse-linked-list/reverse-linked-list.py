# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rvend = None
        curr = head
        while curr != None:
            sec = curr.next
            curr.next = rvend
            rvend = curr
            curr = sec
        return rvend
        