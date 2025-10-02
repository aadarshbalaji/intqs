# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        

        def helper(subset):

            if not subset:
                return None
            if len(subset) == 1:
                preorder.pop(0)
                return TreeNode(subset[0])
            
            new_root = preorder.pop(0)
            new_root_index = subset.index(new_root)
            L_inorder = subset[0:new_root_index]
            R_inorder = subset[new_root_index + 1:]

            new_node = TreeNode(new_root)
            new_node.left = helper(L_inorder)
            new_node.right = helper(R_inorder)
            return new_node
        return helper(inorder)
