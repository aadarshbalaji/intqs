# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def isleaf(node):
            if not node:
                return False
            if node.left or node.right:
                return False
            return True

        ans = []

        def helper(node, leaves):
            if not node:
                return 
            if isleaf(node.left):
                leaves.append(node.left.val)
                node.left = None
            else:
                helper(node.left, leaves)
            if isleaf(node.right):
                leaves.append(node.right.val)
                node.right = None
            else:
                helper(node.right, leaves)
            return leaves

        while root.left or root.right:
            ans.append(helper(root, []))
        
        ans.append([root.val])
        return ans
        
        
        




            

        