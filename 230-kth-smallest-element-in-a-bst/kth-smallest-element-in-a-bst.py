# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        #left center right
        arr = []
        def dfs(node):
            if not node:
                return
            if node.left:
                dfs(node.left)
            arr.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        return arr[k-1]