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
        deep = Node(-10000)
        start = deep
        rv = deep
        mapoldtonew = {}
        copy = head
        while copy:
            node = Node(copy.val)
            mapoldtonew[copy] = node
            deep.next = node
            deep = deep.next
            if copy.random:
                node.random = copy.random
            else:
                node.random = None
            copy = copy.next
        while start:
            if start.random:
                start.random = mapoldtonew[start.random]
            else:
                start.random = None
            start = start.next

        return rv.next