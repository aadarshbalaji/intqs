"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        start = head
        if not head:
            return head
        while head.next:
            if head.child:
                flattenchild = self.flatten(head.child)
                end = flattenchild
                while end.next:
                    end = end.next
                head.next.prev = end
                end.next = head.next
                head.next = flattenchild
                flattenchild.prev = head
                head.child = None
            else:
                head = head.next
        while head.child:
            flattenchild = self.flatten(head.child)
            head.next = flattenchild
            flattenchild.prev = head
            head.child = None
            head = head.next
        return start