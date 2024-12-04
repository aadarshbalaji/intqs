class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.keytonode = {}
        self.first = Node()  # Dummy head
        self.last = Node()   # Dummy tail
        self.first.next = self.last
        self.last.prev = self.first
        self.size = 0
        self.cap = capacity

    def delete(self, key):
        node = self.keytonode[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.keytonode[key]

    def deletefirst(self):
        node = self.first.next  # The least recently used node
        self.delete(node.key)

    def addtoend(self, node):
        temp = self.last.prev
        temp.next = node
        node.prev = temp
        node.next = self.last
        self.last.prev = node

    def get(self, key: int) -> int:
        if key not in self.keytonode:
            return -1
        node = self.keytonode[key]
        self.delete(key)
        self.addtoend(node)
        self.keytonode[key] = node  # Re-insert in case it was removed during delete
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.keytonode:
            # Update existing node
            self.delete(key)
            self.size -= 1  # Adjust size as we'll re-add it below
        
        elif self.size >= self.cap:
            # Delete the least recently used node
            self.deletefirst()
            self.size -= 1

        # Add the new node
        node = Node(key, value)
        self.addtoend(node)
        self.keytonode[key] = node
        self.size += 1
