import time

LRUD = [0 + 1j, 0 - 1j, 1, -1]
LRUD_D: list[complex] = [-1 + 1j, -1 - 1j, -1, 0 + 1j, 0 - 1j, 1 + 1j, 1, 1 - 1j]

def inBounds(i, j, mini, maxi, minj, maxj):
    return mini <= i < maxi and minj <= j < maxj

def readFile(day: int, splitOn: str = "", isTest: bool = False, toStrip: bool = True, toList: bool = True) -> list[str]:
    res = []
    filename = f"txts/day-{day:02}.txt" if not isTest else f"txts/day-{day:02}_test.txt"
    with open(filename, "r") as f:
        for line in f:
            if toStrip:
                line = line.strip()
            if splitOn:
                if splitOn == r"\w":
                    line = line.split()
                else:
                    line = line.split(splitOn)
            if toList:
                line = list(line)
            res.append(line)
    return res

def timeFunction(func):

    def wrapper(*args, **kwargs):
        startTime = time.time()
        res = func(*args, **kwargs)
        print(f"Time taken: {time.time() - startTime}")
        return res
    return wrapper

def printParts(part1, part2):
    print("Part 1: " + str(part1))
    print("Part 2: " + str(part2))