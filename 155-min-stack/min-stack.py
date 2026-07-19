class MinStack(object):

    def __init__(self):
        self.stack = []
        self.monostack = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if not self.monostack or value <= self.monostack[-1]:
            self.monostack.append(value)
        self.stack.append(value)

        

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop()
        if val <= self.monostack[-1]:
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
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()