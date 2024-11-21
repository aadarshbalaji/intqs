# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        rv = []
        def create_parents(parent, node):
            if not node:
                return
            node.parent = parent
            create_parents(node, node.right)
            create_parents(node, node.left)
        create_parents(None, root)
        
        visited = set()
        def search(node, height):
            if not node or node in visited:
                return
            if height == k:
                rv.append(node.val)
            visited.add(node)
            search(node.parent, height+1)
            search(node.left, height+1)
            search(node.right, height+1)
        search(target, 0)
        return rv