class Node:
    def __init__(self, key=None, value=None):
        self.prev = None
        self.key = key
        self.value = value
        self.next = None
    
class LRUCache(object):
    

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.first = Node()
        self.last = Node()
        self.first.next = self.last
        self.last.prev = self.first
        self.keytonode = {}
        self.capacity = capacity
        self.currsize = 0 

    def delete(self, key):
        node = self.keytonode[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.keytonode[key]
        self.currsize -= 1

    def deletefirst(self):
        firstreal = self.first.next 
        self.delete(firstreal.key)

    def deletelastnode(self):
        target = self.last.prev
        self.delete(target.key)

    def addtoend(self, node):
        self.last.prev.next = node
        node.prev = self.last.prev
        self.last.prev = node
        node.next = self.last
        self.keytonode[node.key] = node
        self.currsize += 1
        


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keytonode:
            return -1
        node = self.keytonode[key]
        newnode = Node(node.key, node.value)
        self.delete(key)
        self.addtoend(newnode)
        return node.value

        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        newnode = Node(key, value)
        if key in self.keytonode:
            self.delete(key)
        elif self.currsize >= self.capacity:
            self.deletefirst()
        
        self.addtoend(newnode)

            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)