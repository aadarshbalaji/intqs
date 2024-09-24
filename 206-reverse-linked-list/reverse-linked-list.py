# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        new = ListNode(head.val,None)
        curr = head.next
        while curr:
            new = ListNode(curr.val, new)
            curr = curr.next

        return new