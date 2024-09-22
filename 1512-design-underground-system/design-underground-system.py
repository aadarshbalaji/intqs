class UndergroundSystem(object):

    def __init__(self):
        self.checkin = {}
        self.line = defaultdict(lambda: [0,0])

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.checkin[id] = (stationName, t)

        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        loc = self.checkin[id][0]
        time = self.checkin[id][1]
        self.line[(loc, stationName)] = [self.line[(loc, stationName)][0] + t-time, self.line[(loc, stationName)][1] + 1]
        self.checkin.pop(id)
       
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        tup = (startStation, endStation)
        time, count = self.line[tup]
        #print(float(time)/float(count))
        return float(time)/float(count)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)