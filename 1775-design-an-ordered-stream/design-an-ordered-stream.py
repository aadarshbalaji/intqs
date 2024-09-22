class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.pointer = 1
        self.arr = [0 for _ in range(n+1)]
        

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.arr[idKey] = value
        ans = []
        while self.pointer < len(self.arr) and self.arr[self.pointer] != 0:
            ans.append(self.arr[self.pointer])
            self.pointer += 1
        
        return ans
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)