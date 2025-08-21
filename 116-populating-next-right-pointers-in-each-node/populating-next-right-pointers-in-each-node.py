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
        q = deque()
        q.append(root)
        if not root:
            return
        while q:
            currlevel = []
            for i in range(len(q)):
                node = q.popleft()
                currlevel.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            for i, node in enumerate(currlevel):
                if i + 1 < len(currlevel):
                    node.next = currlevel[i+1]
        return root
