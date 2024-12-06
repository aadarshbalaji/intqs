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
        
        def helper(node, string):
            if not node:
                string += 'None,'
            else:
                string += str(node.val) + ','
                string = helper(node.left, string)
                string = helper(node.right, string)
            return string
        return helper(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(arr):
            if arr[0] == 'None':
                arr.pop(0)
                return None
            node = TreeNode(arr[0])
            arr.pop(0)
            node.left = helper(arr)
            node.right = helper(arr)
            return node
        return helper(data.split(','))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))