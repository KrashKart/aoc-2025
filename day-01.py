from aocutils import readFile, timeFunction, printParts

@timeFunction
def main():
    one, two = 0, 0
    t = False
    l = readFile(1, toList=False, isTest=t)

    counter = 50
    for line in l:
        digits = int(line[1:])
        rots, clicks = divmod(digits, 100)
        temp = counter + clicks if line.startswith("R") else counter - clicks
        if counter % 100 == 0:
            one += 1
        edge = 1 if counter != 0 and not (0 < temp < 100) else 0
        two += rots + edge
        counter = temp % 100
    printParts(one, two)
    
if __name__ == "__main__":
    main()