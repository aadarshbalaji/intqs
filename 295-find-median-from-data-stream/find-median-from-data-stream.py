class MedianFinder:

    def __init__(self):
        self.smallernumbers = [] #negative insertion
        self.largernumbers = [] 

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallernumbers, -num)
        if self.smallernumbers and self.largernumbers and -self.smallernumbers[0] > self.largernumbers[0]:
            heapq.heappush(self.largernumbers, -heapq.heappop(self.smallernumbers))
           
        if len(self.smallernumbers) > len(self.largernumbers) + 1:
            maxofsmallernumbers = -1 * heapq.heappop(self.smallernumbers)
            heapq.heappush(self.largernumbers, maxofsmallernumbers)
        if len(self.largernumbers) > len(self.smallernumbers) + 1:
            minoflargernumbers = heapq.heappop(self.largernumbers)
            heapq.heappush(self.smallernumbers, -minoflargernumbers)
    




    def findMedian(self) -> float:
        if len(self.smallernumbers) > len(self.largernumbers):
            return -self.smallernumbers[0]
        if len(self.largernumbers) > len(self.smallernumbers):
            return self.largernumbers[0]
        else:
            return (-self.smallernumbers[0] + self.largernumbers[0])/2
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()