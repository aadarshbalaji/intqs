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
        def create_parents(parent, node):
            if not node:
                return
            node.parent = parent
            create_parents(node, node.left)
            create_parents(node, node.right)
        create_parents(None, root)
        rv = []
        visited = set()
        def traverse(node, dist):
            if not node or dist > k or node in visited:
                return
            if dist == k:
                rv.append(node.val)
            visited.add(node)
            traverse(node.parent, dist+1)
            traverse(node.left, dist+1)
            traverse(node.right, dist+1)
        traverse(target, 0)
        return rv