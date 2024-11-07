# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        deq = deque()
        curr = head.next
        while curr:
            deq.append(curr)
            curr = curr.next
        
        curr = head
        while len(deq) > 1:
            curr.next = deq.pop()
            curr = curr.next
            curr.next = deq.popleft()
            curr = curr.next
        
        if len(deq) != 0:
            curr.next = deq.pop()
            curr = curr.next
        curr.next = None



        