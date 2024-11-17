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
        if not root:
            return None
        
        q = deque([root])
        while q:
            prev = None
            d = len(q)
            for i in range(d):
                node = q.popleft()
                if prev:
                    prev.next = node
                
                prev = node
                if node.left:
                    q.append(node.left)
                    q.append(node.right)
        
        return root

        