class MinStack:

    def __init__(self):
        self.stack = []
        self.min_at_len = [float('inf')]
        self.num_items = 0
        

    def push(self, val: int) -> None:
        self.num_items += 1
        self.min_at_len.append(0)
        self.min_at_len[self.num_items] = min(self.min_at_len[self.num_items-1],val)
        self.stack.append(val)

        

    def pop(self) -> None:
        self.stack.pop()
        self.num_items -= 1
        

    def top(self) -> int:
        return self.stack[self.num_items-1]
        

    def getMin(self) -> int:
        return self.min_at_len[self.num_items]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()