from aocutils import readFile, timeFunction, printParts
from collections import deque
from scipy.optimize import linprog

def press(state, button):
    return tuple(i ^ (idx in button) for idx, i in enumerate(state))

def bfs(start, desired, buttons):
    q = deque([start])
    mem = {start: 0}
    while q:
        curr = q.popleft()
        steps = mem[curr]
        if curr == desired:
            return steps
        for b in buttons:
            new_state = press(curr, b)
            if new_state not in mem.keys():
                mem[new_state] = steps + 1
                q.append(new_state)
            else:
                mem[new_state] = min(steps + 1, mem[new_state])

@timeFunction
def main():
    one, two = 0, 0
    t = False
    lines = readFile(10, splitOn=" ", toList=False, isTest=t)
    for line in lines:
        desired = tuple(c == "." for c in line[0][1:-1])
        start = tuple(0 for _ in desired)
        buttons = [eval(c[:-1] + ",)") for c in line[1:-1]]
        one += bfs(start, desired, buttons)

        ## heavily adapted this part from reddit
        costs = tuple(1 for _ in buttons)
        joltages = eval(line[-1][1:-1])
        eqs = tuple(tuple(i in b for b in buttons) for i in range(len(joltages)))
        two += int(linprog(costs, A_eq=eqs, b_eq=joltages, integrality=1).fun)
    printParts(one, two)
    
if __name__ == "__main__":
    main()