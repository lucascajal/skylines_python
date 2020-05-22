import random
import matplotlib.pyplot as plt

class Skyline:
    def __init__(self, initialBuildings={}):
        self.buildings = dict(initialBuildings)
        self.calcMeasures()

    def __add__(self, other):
        if type(other) is int:
            skyline1 = {}
            for x in self.buildings:
                skyline1[x + other] = self.buildings[x]
            return Skyline(skyline1)
        
        else:
            skyline1 = self.getSkyline()
            skyline2 = other.getSkyline()
            for xmin in skyline2:
                if (not xmin in skyline1) or (skyline1[xmin] < skyline2[xmin]): skyline1[xmin] = skyline2[xmin]
            return Skyline(skyline1)
    
    def __sub__(self, other):
        skyline1 = {}
        for x in self.buildings:
            skyline1[x - other] = self.buildings[x]
        return Skyline(skyline1)

    def __mul__(self, other):
        if type(other) is int:
            neg = other < 0
            other = abs(other)
            skyline1 = {}
            width = abs(max(self.buildings.keys()) - min(self.buildings.keys())) + 1
            for i in range(other):
                for x in self.buildings:
                    skyline1[width*i + x] = self.buildings[x]
            
            if neg:
                return - Skyline(skyline1) -(width * other)
            else:
                return Skyline(skyline1)
        
        else:
            skyline1 = self.getSkyline()
            skyline2 = other.getSkyline()
            res = {}
            for xmin in skyline2:
                if xmin in skyline1: res[xmin] = min(skyline1[xmin], skyline2[xmin])
            return Skyline(res)
    
    def __rmul__(self, other):
        return self * other
    
    def __neg__(self):
        skyline = self.getSkyline()
        ini = min(skyline.keys())
        end = max(skyline.keys())
        while ini < end:
            if (ini in skyline) and (end in skyline):
                aux = skyline[ini]
                skyline[ini] = skyline[end]
                skyline[end] = aux
            elif ini in skyline:
                skyline[end] = skyline[ini]
                skyline.pop(ini)
            elif end in skyline:
                skyline[ini] = skyline[end]
                skyline.pop(end)
            ini += 1
            end -= 1

        return Skyline(skyline)

    def addBuilding(self, building):
        if self.height < building[1]: self.height = building[1]
        if building[1] > 0:
            for i in range(building[0], building[2]):
                if not i in self.buildings:
                    self.buildings[i] = building[1]
                    self.area += building[1]
                elif self.buildings[i] < building[1]:
                    self.area += building[1] - self.buildings[i]
                    self.buildings[i] = building[1]
    
    def addBuildings(self, buildingList):
        for building in buildingList:
            self.addBuilding(building)
    
    def addRandom(self, n, h, w, xmin, xmax):
        for _ in range(n):
            height = random.randint(0,h)
            width = random.randint(1, min((xmax - xmin), w))
            start = random.randint(xmin, (xmax - width))
            self.addBuilding((start, height, start + width))

    def getSkyline(self):
        return dict(self.buildings)
    
    def calcMeasures(self):
        a = 0
        h = 0
        for x in self.buildings.values():
            a += x
            if (x > h): h = x
        self.area = a
        self.height = h
        return a, h

    def getMeasures(self):
        return self.area, self.height
    
    def printSkyline(self):
        plt.bar(self.buildings.keys(), self.buildings.values(), width=1, align='edge', color=['red'])
        plt.show()