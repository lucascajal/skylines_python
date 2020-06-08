import random
import matplotlib.pyplot as plt
import time
from pathlib import Path


class WrongDimensions(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'WrongDimensions, {0}'.format(self.message)
        else:
            return 'WrongDimensions has been raised'


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
            skyline1 = dict(self.getSkyline())
            skyline2 = other.getSkyline()
            for xmin in skyline2:
                if (xmin not in skyline1) or (skyline1[xmin] < skyline2[xmin]):
                    skyline1[xmin] = skyline2[xmin]
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
            if len(self.buildings.keys()) == 0:
                return Skyline()
            skyline1 = {}
            width = abs(max(self.buildings.keys()) - min(self.buildings.keys())) + 1
            for i in range(other):
                for x in self.buildings:
                    skyline1[width*i + x] = self.buildings[x]

            if neg:
                return - Skyline(skyline1) - (width * other)
            else:
                return Skyline(skyline1)

        else:
            skyline1 = self.getSkyline()
            skyline2 = other.getSkyline()
            res = {}
            if len(skyline1) < len(skyline2):
                for xmin in skyline1:
                    if xmin in skyline2:
                        res[xmin] = min(skyline1[xmin], skyline2[xmin])
            else:
                for xmin in skyline2:
                    if xmin in skyline1:
                        res[xmin] = min(skyline1[xmin], skyline2[xmin])
            return Skyline(res)

    def __rmul__(self, other):
        return self * other

    def __neg__(self):
        if len(self.buildings.keys()) == 0:
            return Skyline()
        skyline = dict(self.getSkyline())
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
        if (building[0] >= building[2]) or (building[1] < 0):
            raise WrongDimensions
        if self.height < building[1]:
            self.height = building[1]
        if building[1] > 0:
            for i in range(building[0], building[2]):
                if i not in self.buildings:
                    self.buildings[i] = building[1]
                    self.area += building[1]
                elif self.buildings[i] < building[1]:
                    self.area += building[1] - self.buildings[i]
                    self.buildings[i] = building[1]

    def addBuildings(self, buildingList):
        for building in buildingList:
            self.addBuilding(building)

    def addRandom(self, n, h, w, xmin, xmax):
        if (n < 0) or (h < 0) or (xmin >= xmax) or (w < 1):
            raise WrongDimensions
        for _ in range(n):
            height = random.randint(0, h)
            width = random.randint(1, min((xmax - xmin), w))
            start = random.randint(xmin, (xmax - width))
            self.addBuilding((start, height, start + width))

    def getSkyline(self):
        return self.buildings

    def calcMeasures(self):
        a = 0
        h = 0
        for x in self.buildings.values():
            a += x
            if (x > h):
                h = x
        self.area = a
        self.height = h
        return a, h

    def getMeasures(self):
        return self.area, self.height

    def getCompressedSkyline(self):
        keys = sorted(self.buildings.keys())
        length = len(keys)
        if length == 0:
            return [], [], []

        positions = [keys[0]]
        heights = []
        widths = []
        w = 1
        for i in range(1, length):
            if (keys[i] == keys[i-1] + 1) and (self.buildings[keys[i]] == self.buildings[keys[i-1]]):
                w += 1
            else:
                heights.append(self.buildings[keys[i-1]])
                widths.append(w)
                w = 1
                positions.append(keys[i])

        heights.append(self.buildings[keys[length-1]])
        widths.append(w)
        return (positions, heights, widths)

    def uncompressSkyline(self, compressed):
        positions, heights, widths = compressed
        for i in range(0, len(positions)):
            self.addBuilding((positions[i], heights[i], positions[i] + widths[i]))

    def printSkyline(self):
        positions, heights, widths = self.getCompressedSkyline()
        if len(positions) == 0:
            plt.bar([0], [0], width=1, align='edge', color=['red'])
            plt.show()
        else:
            plt.bar(positions, heights, width=widths, align='edge', color=['red'])
            plt.show()

    def saveImage(self, user_id):
        positions, heights, widths = self.getCompressedSkyline()
        path = str(Path(__file__).parent) + "/userData/"
        Path(path + user_id).mkdir(parents=True, exist_ok=True)
        if len(positions) == 0:
            plt.bar([0], [0], width=1, align='edge', color=['red'])
            plt.savefig(path + user_id + '/fig.png')
            plt.close()
        else:
            plt.bar(positions, heights, width=widths, align='edge', color=['red'])
            plt.savefig(path + user_id + '/fig.png')
            plt.close()
