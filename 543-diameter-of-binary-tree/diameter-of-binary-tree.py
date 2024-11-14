class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Initialize the global variable here
        global currmax
        currmax = 0  # Set initial value for maximum diameter
        
        def depth(node):
            if not node:
                return 0
            leftd = depth(node.left)
            rightd = depth(node.right)
            
            # Update the global max diameter
            global currmax
            currmax = max(currmax, leftd + rightd)
            
            # Return the depth of this node
            return 1 + max(leftd, rightd)
        
        # Call the depth function
        depth(root)
        
        # Return the maximum diameter found
        return currmax
