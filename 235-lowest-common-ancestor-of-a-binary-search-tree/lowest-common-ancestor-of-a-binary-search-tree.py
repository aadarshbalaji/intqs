# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def search(node):
            if not node or (p.val < node.val < q.val) or (q.val < node.val < p.val):
                return node
            
            if node == p or node == q:
                return node
            
            if p.val < node.val and q.val < node.val:
                return search(node.left)
            
            if p.val > node.val and q.val > node.val:
                return search(node.right)
        return search(root)



        