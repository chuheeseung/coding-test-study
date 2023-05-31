class UndergroundSystem:

    def __init__(self):
        self.datas = []

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.datas.append([id, stationName, t])

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.datas.append([id, stationName, t])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        startTime = 0
        endTime = 0
        time = 0
        count = 0

        for i in range(len(self.datas)):
            if self.datas[i][1] == startStation:  # start
                startTime = self.datas[i][2]
                count += 1
            elif self.datas[i][1] == endStation:  # end
                endTime = self.datas[i][2]
            time += endTime - startTime

        return time / count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)