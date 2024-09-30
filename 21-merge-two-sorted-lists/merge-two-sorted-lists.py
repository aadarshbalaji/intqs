# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1, None)
        curr = dummy
        a = list1
        b = list2
        while a or b:
            if a and not b:
                while a:
                    curr.next = ListNode(a.val, None)
                    curr = curr.next
                    a = a.next
            elif b and not a:
                while b:
                    curr.next = ListNode(b.val, None)
                    curr = curr.next
                    b = b.next
            elif a.val > b.val:
                curr.next = ListNode(b.val, None)
                curr = curr.next
                b = b.next
            else:
                curr.next = ListNode(a.val, None)
                curr = curr.next
                a = a.next
        return dummy.next

                

            