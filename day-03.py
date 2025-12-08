from aocutils import readFile, timeFunction, printParts

def recurse(l, lim):
    if lim == 1:
        return max(l)
    n = len(l) - lim + 1
    largest = max(l[:n])
    return largest * 10 ** (lim - 1) + recurse(l[l.index(largest) + 1:], lim - 1)


@timeFunction
def main():
    one, two = 0, 0
    t = False
    lines = readFile(3, toList=True, isTest=t)
    for l in lines:
        l = list(map(int, l))
        one += recurse(l, 2)
        two += recurse(l, 12)
    printParts(one, two)
    
if __name__ == "__main__":
    main()