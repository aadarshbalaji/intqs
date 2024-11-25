"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        root = p
        while root.parent:
            root = root.parent
        #print(root.val)
        def helper(node, p, q):
            if not node:
                return
            if node == p or node == q:
                return node
            l = helper(node.left, p, q)
            r = helper(node.right, p, q)
            if l and r:
                return node
            return l or r
        return helper(root, p,q)