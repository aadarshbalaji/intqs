"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        realtofake = {}
        nodetorandom = {}
        dummy = Node(-1)
        i = 0
        prev = dummy
        while head:
            newnode = Node(head.val)
            prev.next = newnode
            nodetorandom[newnode] = head.random
            realtofake[head] = newnode
            prev = newnode
            head = head.next
            i += 1
        prev.next = None
        curr = dummy.next
        while curr:
            og = nodetorandom[curr]
            if og is None:
                curr.random = prev.next
            else:
                curr.random = realtofake[og]
            curr = curr.next
        return dummy.next
                
        
