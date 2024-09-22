class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.line = defaultdict(lambda: [0,0])
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        loc, starttime = self.checkin[id]
        x,y = self.line[(loc, stationName)] 
        self.line[(loc, stationName)] = [x+t-starttime, y+1]
        self.checkin.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time,count = self.line[(startStation, endStation)]
        return float(time)/float(count)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)