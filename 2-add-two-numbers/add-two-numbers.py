# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first = 0
        num = 0
        while l1:
            first = first + l1.val * (10 ** num)
            num += 1
            l1 = l1.next
        second = 0
        num = 0
        while l2:
            second = second + l2.val * (10 ** num)
            num += 1
            l2 = l2.next
        
        
        final = first + second
        final = str(final)

        node = ListNode(int(final[0]), None)
        final = final[1:]
        while len(final) > 0:
            node = ListNode(int(final[0]), node)
            final = final[1:]
        return node