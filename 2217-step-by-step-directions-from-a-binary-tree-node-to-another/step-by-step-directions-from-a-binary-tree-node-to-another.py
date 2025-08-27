# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """

        def explore(node, path, target):
            if not node:
                return ''
            if node.val == target:
                return path
            path.append('L')
            currleft = explore(node.left, path, target)
            if currleft:
                return currleft
            path.pop()
            path.append('R')
            currright = explore(node.right, path, target)
            if currright:
                return currright
            path.pop()
                    
        tostart = explore(root, [], startValue)
        toend = explore(root, [], destValue)
        #print(tostart, toend)
        
        i = 0
        while i < len(tostart) and i < len(toend) and tostart[i] == toend[i]:
            i += 1

        rv = ['U' for k in range(len(tostart)-i)]
        for k in range(i, len(toend)):
            rv.append(toend[k])
        return ''.join(rv)

