# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        first = head
        second = head.next
        temp = second
        while second and second.next:
            first.next, second.next = second.next, second.next.next
            second = second.next
            first = first.next
        first.next = temp
        return head