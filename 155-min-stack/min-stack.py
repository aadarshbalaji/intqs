class MinStack(object):

    def __init__(self):
        self.monostack = []
        self.stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.monostack or val <= self.monostack[-1]:
            self.monostack.append(val)
        
        self.stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        popped_val = self.stack.pop()
        if popped_val <= self.monostack[-1]:
            self.monostack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.monostack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()