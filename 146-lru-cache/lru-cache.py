class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.keytoNode = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0
        self.capacity = capacity
    
    def addtotail(self, key, val):
        node = Node(key, val)
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node
        self.keytoNode[key] = node
        self.length += 1
    
    def delete(self, k):
        node = self.keytoNode[k]
        del self.keytoNode[k]
        node.prev.next=node.next
        node.next.prev = node.prev
        self.length -= 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keytoNode:
            return -1
        node = self.keytoNode[key]
        rv = node.val
        self.delete(key)
        self.addtotail(key, rv)
        return rv

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.keytoNode:
            self.delete(key)
            self.addtotail(key, value)
            return
        if self.length == self.capacity:
            sample = self.head.next.key
            self.delete(sample)
        self.addtotail(key,value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)