# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        first = head
        start = head
        length = 1
        while start.next:
            length += 1
            start = start.next
        start.next = first
        number_of_rotations = k % length
        for i in range(length - number_of_rotations):
            head = head.next
        start = head
        for i in range(length-1):
            start = start.next
        start.next = None
        return head


        