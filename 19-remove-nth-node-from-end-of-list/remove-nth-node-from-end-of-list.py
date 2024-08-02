# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        r = ListNode(0,head)
        first = r
        second = head
        for i in range(n):
            second = second.next
        while second:
                first = first.next
                second = second.next
        first.next = first.next.next
        return r.next
        