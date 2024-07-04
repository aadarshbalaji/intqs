# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for linkedlist in lists:
            while linkedlist != None:
                heappush(h,linkedlist.val)
                linkedlist = linkedlist.next
        
        new = ListNode()
        rv = new
        while len(h) != 0:
            node = ListNode(heappop(h))
            new.next = node
            new = new.next
        return rv.next