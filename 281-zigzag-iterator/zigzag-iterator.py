class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.arr1 = v1
        self.arr2 = v2
        self.pointer1 = 0
        self.pointer2 = 0
        self.turn = 0
        

    def next(self):
        """
        :rtype: int
        """
        rv = None
        if self.turn == 0 or self.pointer2 >= len(self.arr2):
            if self.pointer1 < len(self.arr1):
                rv = self.arr1[self.pointer1]
                self.pointer1 += 1
        
        if rv == None or self.turn == 1:
            if self.pointer2 < len(self.arr2):
                rv = self.arr2[self.pointer2]
                self.pointer2  += 1
        
        self.turn = 1 - self.turn
        return rv
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.pointer1 < len(self.arr1) or self.pointer2 < len(self.arr2):
            return True
        return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())