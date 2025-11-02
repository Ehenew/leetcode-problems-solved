class UndergroundSystem:

    def __init__(self):
        self.checkIns = {}        # id -> (stationName, time)
        self.travelData = {}      # (startStation, endStation) -> [totalTime, tripCount]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkIns.pop(id)
        travelTime = t - startTime
        route = (startStation, stationName)

        if route not in self.travelData:
            self.travelData[route] = [0, 0]
        self.travelData[route][0] += travelTime
        self.travelData[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, tripCount = self.travelData[(startStation, endStation)]
        return totalTime / tripCount


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)