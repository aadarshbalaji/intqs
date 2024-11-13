"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return root
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            n = list(q)
            for i in range(0, len(n)-1):
                n[i].next = n[i+1]
            q = deque()
            for nnn in n:
                if nnn.left:
                    q.append(nnn.left)
                if nnn.right:
                    q.append(nnn.right)
        return root
        

        