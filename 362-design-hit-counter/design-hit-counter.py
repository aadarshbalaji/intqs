class HitCounter(object):

    def __init__(self):
        self.deq = deque()

    def hit(self, timestamp):
        """
        :type timestamp: int
        :rtype: None
        """
        self.deq.append(timestamp)
        

    def getHits(self, timestamp):
        """
        :type timestamp: int
        :rtype: int
        """
        while self.deq and self.deq[0] <= (timestamp - 300):
            self.deq.popleft()
        return len(self.deq)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)