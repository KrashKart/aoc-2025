from aocutils import readFile, timeFunction, printParts
from shapely import Polygon, box

@timeFunction
def main():
    one, two = 0, 0
    t = False
    lines = readFile(9, splitOn=",", toList=False, isTest=t)
    lines = list(map(lambda x: tuple(map(int, x)), lines))

    p = Polygon(lines)
    for i in range(len(lines) - 1):
        a = lines[i]
        for j in range(i + 1, len(lines)):
            b = lines[j]
            area = (abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1)
            one = max(one, area)
            rect = box(min(a[0], b[0]), min(a[1], b[1]), max(a[0], b[0]), max(a[1], b[1]))
            if p.contains(rect):
                two = max(two, area)
    printParts(one, two)
    
if __name__ == "__main__":
    main()