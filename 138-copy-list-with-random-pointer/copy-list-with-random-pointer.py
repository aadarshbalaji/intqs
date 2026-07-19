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
        if not head:
            return 
        real_to_dup = {}
        real_to_dup[None] = None
        temp_head = head
        another_head = head
        while head:
            head_copy = Node(head.val)
            real_to_dup[head] = head_copy
            head = head.next
        while temp_head:
            real_to_dup[temp_head].next = real_to_dup[temp_head.next]
            real_to_dup[temp_head].random = real_to_dup[temp_head.random]
            temp_head = temp_head.next
        return real_to_dup[another_head]
            