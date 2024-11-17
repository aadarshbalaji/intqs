class RandomizedSet(object):
    import random 
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
        self.hs[val] = len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.hs:
            return False
        index = self.hs[val]
        temp = self.arr[-1]
        self.arr[index] = temp
        self.hs[temp] = index
        del self.hs[val]
        self.arr.pop()
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        index = random.randint( 0, len(self.arr)-1)
        return self.arr[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()