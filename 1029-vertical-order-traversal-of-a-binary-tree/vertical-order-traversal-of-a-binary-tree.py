# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hs = defaultdict(list)
        currmax = -float('inf')
        currmin = float('inf')
        def search(node, x, y):
            if not node:
                return
            nonlocal currmax
            currmax = max(currmax, y)
            nonlocal currmin
            currmin = min(currmin, y)
            hs[y].append([x,y,node.val])
            search(node.right,x+1, y + 1)
            search(node.left,x+1, y - 1)
        search(root, 0, 0)
        for arr in hs.values():
            arr.sort(key = lambda x: (x[0], x[2]))
        rv = []
        for i in range(currmin, currmax+1):
            rv.append([xxx[-1] for xxx in hs[i]])
        return rv
