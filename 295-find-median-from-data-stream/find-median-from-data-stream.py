class MedianFinder(object):

    def __init__(self):
        self.smallernumbers = [] #negative insertion
        self.largernumbers = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.smallernumbers, -num)
        if self.largernumbers and self.smallernumbers:
            if (-1 * self.smallernumbers[0]) > self.largernumbers[0]:
                heapq.heappush(self.largernumbers, -heapq.heappop(self.smallernumbers)) 
        if len(self.smallernumbers) > len(self.largernumbers) + 1:
            val = -heapq.heappop(self.smallernumbers)
            heapq.heappush(self.largernumbers, val)
        if len(self.largernumbers) > len(self.smallernumbers) + 1:
            val = heapq.heappop(self.largernumbers)
            heapq.heappush(self.smallernumbers, -val)
    def findMedian(self):
        """
        :rtype: float
        """
        #print(self.smallernumbers)
       # print(self.largernumbers)
        if len(self.smallernumbers) > len(self.largernumbers):
            val = -1 * self.smallernumbers[0]
            return val
            
        elif len(self.largernumbers) > len(self.smallernumbers):
            return self.largernumbers[0]
        else:
            maxofsmall = -self.smallernumbers[0]
            minoflarge = self.largernumbers[0]
            return (float(maxofsmall) + float(minoflarge))/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()