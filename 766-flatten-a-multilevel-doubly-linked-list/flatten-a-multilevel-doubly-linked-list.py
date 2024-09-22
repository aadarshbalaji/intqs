"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            print('h')
            return head
        start = head
        while head.next:
            if head.child:
                flattenchild = self.flatten(head.child)
                end = flattenchild
                while end.next:
                    end = end.next
                end.next = head.next
                head.next.prev = end
                head.next = flattenchild
                flattenchild.prev = head
                head.child = None
                head = end
            head = head.next
        while head.child:
            flattenchild = self.flatten(head.child)
            head.next = flattenchild
            flattenchild.prev = head
            head.child = None
            head = head.next
            
        return start