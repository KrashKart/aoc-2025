from aocutils import readFile, timeFunction, printParts
from ufds import DisjointSet
from heapq import heappush, heappop
from math import *

@timeFunction
def main():
    one, two = 0, 0
    t = False
    lines = readFile(8, splitOn=",", toList=True, isTest=t)
    lines = list(map(lambda x: tuple(map(int, x)), lines))
    ufds = DisjointSet()
    dists = []
    for i in range(len(lines) - 1):
        for j in range(i + 1, len(lines)):
            heappush(dists, (dist(lines[i], lines[j]), i, j))
    c = 0
    while True:
        p = heappop(dists)
        if lines[p[1]] not in ufds.find(lines[p[2]]):
            ufds.union(lines[p[1]], lines[p[2]])
            c += 1
        if c == 1000:
            one = prod(sorted(map(len, ufds), reverse=True)[:3])
        if len(list(ufds)[0]) == 1000:
            two = lines[p[1]][0] * lines[p[2]][0]
            break
    printParts(one, two)
    
if __name__ == "__main__":
    main()