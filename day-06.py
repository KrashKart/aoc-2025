from aocutils import readFile, timeFunction, printParts
from operator import add, mul

@timeFunction
def main():
    one, two = 0, 0
    t = False
    lines = readFile(6, splitOn=r"\w", toList=False, isTest=t)
    op = list(map(lambda x: mul if x == "*" else add, lines[-1]))

    # part 1
    lines = list(map(lambda x: list(map(int, x)), lines[:-1]))
    arr = lines[0][:]
    for line in lines[1:]:
        for i in range(len(line)):
            arr[i] = op[i](arr[i], line[i])
    one = sum(arr)

    # part 2
    lines_s = readFile(6, splitOn="", toStrip=False, toList=True, isTest=t)[:-1]
    lines_s = list(map(list, zip(*lines_s)))[:-1]
    arrTwo, i = [0 if op[r] == add else 1 for r in range(len(op))], 0
    for l in lines_s:
        curr = list(filter(lambda x: x != " ", l))
        num = 0
        if not curr:
            i += 1
        else:
            for j in curr:
                num *= 10
                num += int(j)
            arrTwo[i] = op[i](arrTwo[i], num)
    two = sum(arrTwo)
    printParts(one, two)
    
if __name__ == "__main__":
    main()