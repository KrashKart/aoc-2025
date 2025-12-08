from aocutils import readFile, timeFunction, printParts, LRUD_D, inBounds

@timeFunction
def main():
    one, two = 0, 0
    t = False
    lines = readFile(7, toList=True, isTest=t)
    beams = [0 for _ in range(len(lines[0]))]
    for line in lines:
        for i, l in enumerate(line):
            if l == "S":
                beams[i] = 1
            elif l == "^" and beams[i] > 0:
                beams[i + 1] += beams[i]
                beams[i - 1] += beams[i]
                beams[i] = 0
                one += 1
    two = sum(beams)
    printParts(one, two)
    
if __name__ == "__main__":
    main()