import random

# adjacencyList = {
#     1: [2, 3, 4],
#     2: [1, 3, 4],
#     3: [1, 2, 4],
#     4: [1, 2, 3]
# }

# adjacencyList = {
#     1: [2, 3],
#     2: [1, 4],
#     3: [1, 4],
#     4: [2, 3]
# }

# adjacencyList = {
#     1: [2, 3, 4],
#     2: [1, 3, 4],
#     3: [1, 2, 4, 5],
#     4: [1, 2, 3, 6],
#     5: [3, 6, 8, 7],
#     6: [4, 5, 7, 8],
#     7: [5, 6, 8],
#     8: [5, 6, 7]
# }

def measureCut(adjacencyList):
    return len(adjacencyList[list(adjacencyList.keys())[0]])

def contract(adjacencyList):
    # get random graph vertex
    randVertex = random.choice(list(adjacencyList.keys()))
    # print("==========================================")
    # print("Random vertex: {0}".format(randVertex))
    endpoints = adjacencyList[randVertex]

    # get random adjacent vertex
    randEndpoint = random.choice(endpoints)
    # print("Random edge: {0} -> {1}".format(randVertex, randEndpoint))
    # print("Random vertex adjacent vertices: {0}".format(adjacencyList[randVertex]))
    # print("Random endpoint adjacent vertices: {0}".format(adjacencyList[randEndpoint]))

    # delete randomly selected graph edge
    adjacencyList[randVertex].remove(randEndpoint)
    adjacencyList[randEndpoint].remove(randVertex)
    for i in adjacencyList[randVertex]:
        for index, j in enumerate(adjacencyList[i]):
            if j == randVertex:
                adjacencyList[i][index] = randEndpoint
    adjacencyList[randEndpoint] = adjacencyList[randEndpoint] + adjacencyList[randVertex]
    #print("Merged Random endpoint adjacent vertices: {0}".format(adjacencyList[randEndpoint]))

    #remove loops
    while randEndpoint in adjacencyList[randEndpoint]:
        adjacencyList[randEndpoint].remove(randEndpoint)
    #print("Merged Random endpoint adjacent vertices without loops: {0}".format(adjacencyList[randEndpoint]))

    # delete randomly selected vertex
    del adjacencyList[randVertex]

    adjacencyList


adjacencyList = {}
with open("kargerMinCut.txt") as f:
    for l in f.readlines():
        values = l.split("\t")
        adjacencyList[values[0]] = values[1:-1]

cuts = []
for run in range(0, 200):
    runAdjacencyList = {}
    for key in adjacencyList:
        runAdjacencyList[key] = adjacencyList[key].copy()

    while len(runAdjacencyList.keys()) > 2:
        contract(runAdjacencyList)
    #print("Adjacency list: {0}".format(runAdjacencyList))
    print("Cut: {0}".format(measureCut(runAdjacencyList)))
    cuts.append(measureCut(runAdjacencyList))

print("Cuts: {0}".format(cuts))
print("Min cut: {0}".format(min(cuts)))