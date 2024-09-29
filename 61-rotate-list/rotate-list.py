# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        start = head
        count = 1
        while start.next:
            count += 1
            start = start.next
        start.next = head
        k = count - k % count
        final = head
        for i in range(k):
            final = final.next
        new = final
        for i in range(count-1):
            new = new.next
        new.next = None
        return final
        