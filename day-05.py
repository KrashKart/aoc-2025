from aocutils import readFile, timeFunction, printParts

def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    out = []
    prev = intervals[0]
    for interval in intervals[1:]:
        if interval[0] <= prev[1]:
            prev[1] = max(prev[1], interval[1])
        else:
            out.append(prev)
            prev = interval
    
    out.append(prev)
    return out

@timeFunction
def main():
    one, two = 0, 0
    t = False
    lines = readFile(5, toList=False, isTest=t)
    intervals, ingredients = lines[:lines.index("")], lines[lines.index("") + 1:]
    intervals = merge(list(map(lambda x: list(map(int, x.split("-"))), intervals)))
    ingredients = list(map(int, ingredients))

    for i in ingredients:
        for j in intervals:
            if j[0] <= i <= j[1]:
                one += 1
                break
    
    for j in intervals:
        two += j[1] - j[0] + 1
    printParts(one, two)
    
if __name__ == "__main__":
    main()