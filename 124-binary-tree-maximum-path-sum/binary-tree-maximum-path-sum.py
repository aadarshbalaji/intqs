# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = [-float('inf')]
        def max_gain(node):

            if not node:
                return 0
            max_gain_left = max(max_gain(node.left),0)
            max_gain_right = max(max_gain(node.right), 0)

            total_max = max(max_gain_right + node.val, max_gain_left + node.val)
            max_sum[0] = max(max_sum[0], max_gain_right + max_gain_left + node.val)
            return total_max
        
        max_gain(root)
        return max_sum[0]

