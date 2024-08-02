"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new = Node(-10, None, None)
        copynew = new
        mappings = {None:None}
        copy = head
        while head:
            test = Node(head.val)
            new.next = test
            mappings[head] = test
            head=head.next
            new = new.next
        copynew = copynew.next
        rv = copynew
        while copy:
            randval = mappings[copy.random]
            copynew.random = randval
            copy = copy.next
            copynew = copynew.next
        return rv



        