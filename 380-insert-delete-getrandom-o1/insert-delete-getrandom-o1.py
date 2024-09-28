class RandomizedSet:

    def __init__(self):
        self.hs = {} #maps value to index
        self.arr = [] #holds values

    def insert(self, val: int) -> bool:
        if val in self.hs:
            return False
        self.hs[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hs:
            return False
        valindex = self.hs[val]
        lastval = self.arr[-1]
        self.hs[lastval] = valindex
        self.arr[valindex] = lastval
        self.arr.pop(-1)
        self.hs.pop(val)
        return True


    def getRandom(self) -> int:
        index = random.randint(0,len(self.arr)-1)
        return self.arr[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()