edges = set()
weights = {}

with open("dijkstraData.txt") as f:
    for l in f.readlines():
        values = l.split("\t")
        first = int(values[0])
        for v in values[1:-1]:
            pair = v.split(",")
            edge = (first, int(pair[0]))
            weights[edge] = int(pair[1])
            edges.add(edge)


def getAdjacencyList(edges, isReversed = False):
    adjacencyList = {}
    first = 0 if not isReversed else 1
    second = 1 if not isReversed else 0
    for edge in edges:
        if edge[first] not in adjacencyList:
            adjacencyList[edge[first]] = []
        if edge[second] not in adjacencyList:
            adjacencyList[edge[second]] = []
        adjacencyList[edge[first]].append(edge[second])
    return adjacencyList

# edges = set([(1, 2), (2, 4), (1, 3), (3, 4), (3, 2)])
# weights = {(1, 2): 8, (2, 4): 3, (1, 3): 4, (3, 4): 7, (3, 2): 1}
adjacencyList = getAdjacencyList(edges)

def dijkstra(sourceVertex, adjacencyList, edges, weights):
    vertices = set(adjacencyList.keys())
    vertices.remove(sourceVertex)
    processed = set([sourceVertex])
    dists = {sourceVertex: 0}
    while len(vertices) > 0:
        best = None
        for edge in edges:
            if edge[0] in processed and edge[1] in vertices:
                score = dists[edge[0]] + weights[edge]
                if best is None or score < best[0]:
                    best = score, edge
        if best is not None:
            edges.remove(best[1])
            vertices.remove(best[1][1])
            processed.add(best[1][1])
            dists[best[1][1]] = best[0]
    return dists

dists = dijkstra(1, adjacencyList, edges, weights)
print(dists)

vertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
distsSubset = list(map(lambda x: dists.get(x, 1000000), vertices))
print(distsSubset)