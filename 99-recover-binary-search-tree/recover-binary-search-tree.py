# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            curr.append([node, node.val])
            traverse(node.right)
        traverse(root)
        if not curr:
            return
        first_swap = None
        second_swap = None

        for i in range(len(curr) - 1):
            if curr[i][1] > curr[i + 1][1]:
                if first_swap is None:
                    first_swap = curr[i][0]
                second_swap = curr[i + 1][0]

        #print(first_swap.val, second_swap.val)
        if not first_swap or not second_swap:
            return
        #print('ehalsdfa')
        #print(first_swap.val, second_swap.val)
        first_swap.val, second_swap.val = second_swap.val, first_swap.val
        

        