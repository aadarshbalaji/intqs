class RandomizedSet(object):

    def __init__(self):
        self.hs = {}
        self.arr = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.hs:
            return False
        else:
            self.hs[val] = len(self.arr) 
            self.arr.append(val)
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.hs:
            last = self.arr[-1]
            index = self.hs[val]
            self.arr[index] = last
            self.hs[last] = index
            self.arr[-1] = val
            self.arr.pop()
            self.hs.pop(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        ind = random.randint(0, len(self.arr)-1)
        return self.arr[ind]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()