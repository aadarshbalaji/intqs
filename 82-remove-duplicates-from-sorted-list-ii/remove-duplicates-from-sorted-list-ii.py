# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #''D --> 1 --> 1 -- > 2 -- > 2''
        dummy = ListNode(-10)
        dummy.next = head
        prev = dummy
        check = dummy.next
        while check:
            temp_val = check.val
            temp = check
            if temp.next and temp.next.val == temp_val:
                while temp.next and temp.next.val == temp_val:
                    temp = temp.next
                prev.next = temp.next
                check = temp.next
            else:
                prev = temp
                check = temp.next
        return dummy.next