class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hs = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.hs:
            self.hs.move_to_end(key)
            return self.hs[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hs:
            self.hs.move_to_end(key)
        self.hs[key] = value
        if len(self.hs) > self.cap:
            self.hs.popitem(False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)