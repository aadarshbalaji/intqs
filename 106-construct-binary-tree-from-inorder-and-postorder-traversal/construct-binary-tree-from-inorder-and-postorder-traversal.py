# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not inorder or not postorder:
            return None
        n = postorder.pop()
        node = TreeNode(n)
        i = inorder.index(n)
        node.right = self.buildTree(inorder[i+1:], postorder)
        node.left = self.buildTree(inorder[0:i], postorder)
        return node