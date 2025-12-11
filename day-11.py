from aocutils import readFile, timeFunction, printParts
import igraph as ig

def dfs(edges: dict, start, end):
    ref = {end: 1}

    while start not in ref.keys():
        for node in edges.keys():
            if node not in ref and all(n in ref.keys() for n in edges.get(node, tuple())):
                ref[node] = sum(ref[n] for n in edges.get(node, ()))
    return ref[start]

@timeFunction
def main_dfs():
    one, two = 0, 0
    t = False
    lines = readFile(11, toList=False, isTest=t)
    E = {}
    for line in lines:
        u, vs = line.split(":")
        u, vs = u.strip(), tuple(map(lambda x: x.strip(), vs.strip().split(" ")))
        E[u] = vs
    E["out"] = tuple()
    one = dfs(E, "you", "out")
    two = dfs(E, "svr", "dac") * dfs(E, "dac", "fft") * dfs(E, "fft", "out") 
    two += dfs(E, "svr", "fft") * dfs(E, "fft", "dac") * dfs(E, "dac", "out")
    printParts(one, two)

# Too long!
@timeFunction
def main_ig():
    one, two = 0, 0
    t = False
    lines = readFile(11, toList=False, isTest=t)
    G = ig.Graph(directed=True)
    for line in lines:
        u, vs = line.split(":")
        u, vs = u.strip(), list(map(lambda x: x.strip(), vs.strip().split(" ")))
        G.add_vertices([u, *vs])
        G.add_edges([(u, v) for v in vs])
    one = len(G.get_all_simple_paths("you", "out"))
    two = len(G.get_all_simple_paths("svr", "dac")) * len(G.get_all_simple_paths("dac", "fft")) \
        * len(G.get_all_simple_paths("fft", "out")) + len(G.get_all_simple_paths("svr", "fft")) \
        * len(G.get_all_simple_paths("fft", "dac")) * len(G.get_all_simple_paths("dac", "out"))
    printParts(one, two)
    del G
    
if __name__ == "__main__":
    main_dfs()
    # main_ig()