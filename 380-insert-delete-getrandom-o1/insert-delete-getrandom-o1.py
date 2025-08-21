class RandomizedSet(object):

    def __init__(self):
        self.arr = []
        self.map = {}
        self.size = 0

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            return False
        self.map[val] = self.size
        self.arr.append(val)
        self.size += 1
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            return False
    
        index = self.map[val]
        if len(self.arr) > 1:
            endval = self.arr[-1]
            endindex = len(self.arr) - 1
            self.arr[index] = endval
            self.map[endval] = index
            del self.map[val]
            self.arr.pop()
            self.size -= 1
        elif len(self.arr) == 1:
            del self.map[val]
            self.arr.pop()
            self.size -= 1
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        index = randint(0, self.size-1)
        return self.arr[index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()