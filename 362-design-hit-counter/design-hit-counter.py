class HitCounter(object):

    def __init__(self):
        self.deq = deque()
        self.hits = 0

    def hit(self, timestamp):
        """
        :type timestamp: int
        :rtype: None
        """
        if self.deq and self.deq[-1][0] == timestamp:
            self.deq[-1][1] += 1
        else:
            self.deq.append([timestamp, 1])
        self.hits += 1
        

    def getHits(self, timestamp):
        """
        :type timestamp: int
        :rtype: int
        """
        print(self.deq)
        while self.deq and self.deq[0][0] <= (timestamp - 300):
            time, numhits = self.deq.popleft()
            self.hits -= numhits
        return self.hits
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)