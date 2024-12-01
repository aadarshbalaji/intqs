# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        preorder = deque(preorder)

        def build(pre, inord):
            if inord:
                root = pre.popleft()
                for i in range(len(inord)):
                    if inord[i] == root:
                        break
                node = TreeNode(root)
                node.left = build(pre, inord[:i])
                node.right = build(pre, inord[i+1:])
                return node
        
        return build(preorder, inorder)