class RandomizedSet:

    def __init__(self):
        self.hs = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.hs:
            return False
        self.hs[val] = len(self.arr)
        self.arr.append(val)
        return True


    def remove(self, val: int) -> bool:
        if val not in self.hs:
            return False
        last = self.arr[-1]
        index = self.hs[val]
        self.arr[index] = last
        self.hs[last] = index
        self.arr[-1] = val
        self.arr.pop()
        self.hs.pop(val)
        return True
        

    def getRandom(self) -> int:
        #print(self.arr)
        ind = random.randint(0,len(self.arr)-1)
        return self.arr[ind]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()