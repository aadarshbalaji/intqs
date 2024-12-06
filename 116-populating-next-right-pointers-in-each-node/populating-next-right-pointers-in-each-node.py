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
            return root
        q = deque()
        q.append(root)
        while q:
            curr =[]
            for i in range(len(q)):
                node = q.popleft()
                curr.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            curr.append(None)
            for i in range(len(curr)-1):
                curr[i].next = curr[i+1]
        return root
                