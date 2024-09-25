class OrderedStream:

    def __init__(self, n: int):
        self.pointer = 1
        self.arr = [0] * (n+1)



    def insert(self, idKey: int, value: str) -> List[str]:
        ans = []
        self.arr[idKey] = value
        while self.pointer < len(self.arr) and self.arr[self.pointer] != 0:
            ans.append(self.arr[self.pointer])
            self.pointer += 1
        return ans



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)