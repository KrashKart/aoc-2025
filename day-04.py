from aocutils import readFile, timeFunction, printParts, LRUD_D, inBounds

def one_iter(lines, I, J, swap_out=False):
    counter = 0
    for i in range(I):
            for j in range(J):
                if lines[i][j] == "@":
                    count = 0
                    for dir in LRUD_D:
                        di, dj = i + int(dir.real), j + int(dir.imag)
                        if inBounds(di, dj, 0, I, 0, J) and lines[di][dj] == "@":
                            count += 1
                    if count < 4:
                        counter += 1
                        if swap_out:
                            lines[i][j] = "."
    return counter

@timeFunction
def main():
    one, two = 0, 0
    t = False
    lines = readFile(4, toList=True, isTest=t)
    I, J = len(lines), len(lines[0])
    one = one_iter(lines, I, J, False)
    while True:
        temp = one_iter(lines, I, J, True)
        if not temp:
            break
        two += temp
    printParts(one, two)
    
if __name__ == "__main__":
    main()