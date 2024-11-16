# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        rv = []
        def traversal(node, path, currsum):
            if not node:
                return
            newsum = currsum + node.val
            if not node.left and not node.right and newsum == targetSum:
                rv.append(list(path))
            if node.left:
                traversal(node.left, list(path) + [node.left.val], newsum)
            if node.right:
                traversal(node.right, list(path) + [node.right.val], newsum)
        if not root:
            return []
        traversal(root, [root.val], 0)
        return rv
            
