# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hs = set()
        while headA or headB:
            if headA:
                if headA in hs:
                    return headA
                hs.add(headA)
                headA = headA.next
            if headB:
                if headB in hs:
                    return headB
                hs.add(headB)
                headB = headB.next
        return None
