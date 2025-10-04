# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        string = [""]
        def dfs(node):
            if not node:
                string[0] += 'N,'
                return
            
            string[0] += str(node.val) + ','
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        #print(string[0])
        return string[0]
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')

        def create(l):
            if not l:
                return None
            if l[0] == 'N':
                l.pop(0)
                return None
            node = TreeNode(l.pop(0))
            node.left = create(l)
            node.right = create(l)
            return node
        
        return create(data)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))