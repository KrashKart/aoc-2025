from aocutils import readFile, timeFunction, printParts, LRUD_D, inBounds

def parse_input(lines):
    presents = []
    grids = []
    requirements = []
    curr_present = []
    present_count = 0
    for l in lines:
        if present_count == 6:
            g, r = l.split(":")
            g, r = tuple(map(eval, g.strip().split("x"))), tuple(map(lambda x: eval(x.strip()), r.strip().split()))
            grids.append(g)
            requirements.append(r)
        else:
            if l and not l[0].isdigit():
                curr_present.append(list(l))
            elif not l:
                presents.append(curr_present)
                curr_present = []
                present_count += 1
    return presents, grids, requirements

@timeFunction
def main():
    one, two = 0, 0
    t = False
    lines = readFile(12, toList=False, isTest=t)
    _, g, r = parse_input(lines)
    for (w, h), req in zip(g, r):
        if (w // 3) * (h // 3) >= sum(req):
            one += 1
    printParts(one, two)
    
if __name__ == "__main__":
    main()