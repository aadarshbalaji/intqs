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
        deq = collections.deque()
        currnode = head.next
        while currnode:
            deq.append(currnode)
            currnode = currnode.next
        
        currnode = head
        while len(deq) >= 2:
            currnode.next = deq.pop()
            currnode = currnode.next
            currnode.next = deq.popleft()
            currnode = currnode.next
        if deq:
            currnode.next = deq.pop()
            currnode = currnode.next
        currnode.next = None

        