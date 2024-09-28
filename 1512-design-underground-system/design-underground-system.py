class UndergroundSystem:

    def __init__(self):
        self.checkins = {} #id to time,station 
        self.lines = defaultdict(lambda: [0,0]) #start, stop to count,time

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, starttime = self.checkins[id]
        self.lines[(startStation, stationName)][0] += 1
        self.lines[(startStation, stationName)][1] += t-starttime
        self.checkins.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        count, time = self.lines[(startStation, endStation)]
        return time/count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)