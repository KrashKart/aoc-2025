import time

def readFile(day: int, splitOn: str = "", isTest: bool = False, toList: bool = True) -> list[str]:
    res = []
    filename = f"day-{day:02}.txt" if not isTest else f"day-{day:02}_test.txt"
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if splitOn:
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