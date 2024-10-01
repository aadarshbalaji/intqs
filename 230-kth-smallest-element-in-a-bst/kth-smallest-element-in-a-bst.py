# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        arr = []
        def search(node):
            #left middle right
            if node.left:
                search(node.left)
            if node:
                arr.append(node.val)
                if len(arr) >= k:
                    return arr[-1]
            if node.right:
                search(node.right)
        search(root)
        return arr[k-1]
        