from skyline import Skyline

'''
a = [(1,2,3),(5,3,6),(6,4,8)]
b = [(2,4,3),(3,1,5)]

sk1 = Skyline()
sk1.addBuildings(a)
#sk1.printSkyline()

sk2 = Skyline()
sk2.addBuildings(b)
#sk2.printSkyline()

sk3 = sk1 + sk2
sk3.printSkyline()

sk3 = - sk3
sk3.printSkyline()
'''

a = Skyline()

a.addBuilding((1,2,3))
print(a.getMeasures())
a.printSkyline()

a.addBuilding((3,4,6))
print(a.getMeasures())
a.printSkyline()

a = a * 3
print(a.getMeasures())
a.printSkyline()

a = -a
print(a.getMeasures())
a.printSkyline()

a = a * 2
print(a.getMeasures())
a.printSkyline()