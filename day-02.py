from aocutils import readFile, timeFunction, printParts

def isInvalid(s, length):
    target = s[:length]
    for i in range(0, len(s), length):
        if s[i:i+length] != target:
            return False
    return True

@timeFunction
def main():
    one, two = 0, 0
    t = False
    lines = readFile(2, splitOn=",", toList=False, isTest=t)[0]
    
    for l in lines:
        l = l.split("-")
        start, end = int(l[0]), int(l[1])
        for n in range(start, end + 1):
            s = str(n)
            for i in range(len(s) // 2, 0, -1):
                if isInvalid(s, i):
                    if i == len(s) / 2:
                        one += n
                    two += n
                    break

    printParts(one, two)
    
if __name__ == "__main__":
    main()