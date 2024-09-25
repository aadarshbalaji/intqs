class RandomizedSet:

    def __init__(self):
        self.s = []
        self.hs = {}

    def insert(self, val: int) -> bool:
        if val in self.hs:
            return False
        else:
            self.hs[val] = len(self.s)
            self.s.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.hs:
            return False
        else:
            index = self.hs[val]
            lastval = self.s[-1]
            self.s[index] = lastval
            self.hs[lastval] = index
            self.s.pop(-1)
            self.hs.pop(val)
            return True

    def getRandom(self) -> int:
        index = random.randint(0,len(self.s)-1)
        return self.s[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()