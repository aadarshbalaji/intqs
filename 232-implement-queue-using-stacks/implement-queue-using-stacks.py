class MyQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.nextpop = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.nextpop:
            self.nextpop = x
        self.s1.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        rv = self.nextpop
        if len(self.s1) == 1:
            self.s1 = []
            self.nextpop = None
            return rv
        while len(self.s1) > 1:
            self.s2.append(self.s1.pop())
        
        self.nextpop = self.s2[-1]
        self.s1 = []
        for _ in range(len(self.s2)):
            self.s1.append(self.s2.pop())
        return rv

        

    def peek(self):
        """
        :rtype: int
        """
        return self.nextpop

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.s1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()