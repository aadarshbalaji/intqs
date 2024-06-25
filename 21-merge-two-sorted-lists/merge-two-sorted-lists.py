# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        rv = ListNode()
        start = rv
        while list1 != None and list2 != None:
            x = list1.val
            y = list2.val
            if x <= y:
                rv.next = ListNode(x)
                rv = rv.next
                list1 = list1.next
            elif y < x:
                rv.next = ListNode(y)
                rv = rv.next
                list2 = list2.next
        if list1 != None:
            rv.next = list1
        if list2 != None:
            rv.next = list2
        return start.next
            
            
        