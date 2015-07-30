from collections import deque

edges = []

with open("SCC.txt") as f:
    for l in f.readlines():
        values = l.split(" ")
        edges.append((int(values[0]), int(values[1])))

# adjacencyList = {
#     1: [5],
#     2: [3],
#     3: [4],
#     4: [2, 5],
#     5: [6],
#     6: [1, 9],
#     7: [8],
#     8: [9],
#     9: [7]
# }

#edges = [(1, 5), (2, 3), (3, 4), (4, 2), (4, 5), (5, 6), (6, 1), (6, 9), (7, 8), (8, 9), (9, 7)]


#edges = [(7, 1), (1, 4), (4, 7), (9, 7), (9, 3), (3, 6), (6, 9), (8, 6), (2, 8), (5, 2), (8, 5), (10, 2)]
#edges = [(1, 2), (2, 3)]


#edges = [(1, 2), (2, 1), (2, 4), (4, 2), (1, 3), (3, 1), (3, 4), (4, 3), (3, 5), (5, 3), (4, 5), (5, 4), (4, 6), (6, 4), (5, 6), (6, 5)]
#edges = [(1, 2), (2, 4),  (1, 3), (3, 4), (3, 5), (4, 5), (4, 6), (5, 6)]

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

adjacencyList = getAdjacencyList(edges)
reversedAdjacencyList = getAdjacencyList(edges, True)

def BFS(adjacencyList, startNode):
    exploredList = {startNode: 0}
    finishTime = 1
    queue = deque([startNode])
    while len(queue) > 0:
        v = queue.popleft()
        for w in adjacencyList[v]:
            if w not in exploredList:
                exploredList[w] = finishTime
                queue.append(w)
                finishTime += 1
    return exploredList

def DFS(adjacencyList, startNode, exploredList, finishTime, finishTimes):
    stack = [startNode]
    while len(stack) > 0:
        v = stack[-1]
        canMove = False
        if v in adjacencyList:
            for w in adjacencyList[v]:
                if w not in exploredList:
                    exploredList[w] = True
                    stack.append(w)
                    canMove = True
        if not canMove:
            v = stack.pop()
            finishTimes[finishTime] = v
            finishTime += 1
    return exploredList, finishTime

# exploredList = {}
# finishTimes = {}
# DFS(adjacencyList, 1, exploredList, 1, finishTimes)
# print(finishTimes)

def DFSLoop(adjacencyList, nodes):
    exploredList = {}
    finishTime = 1
    finishTimes = {}
    sccs = {}
    for node in nodes:
        prevExploredCount = len(exploredList)
        if node not in exploredList:
            exploredList[node] = True
            exploredList, finishTime = DFS(adjacencyList, node, exploredList, finishTime, finishTimes)
            #print(exploredList)
        diff = len(exploredList) - prevExploredCount
        if diff > 0:
            sccs[node] = diff
    return exploredList, finishTimes, sccs

# 1st DFS loop: calculates finishing times
exploredList, finishTimes, sccs = DFSLoop(reversedAdjacencyList, adjacencyList.keys())
# 2nd DFS loop: calculates SCCs
nodes = [finishTimes[key] for key in sorted(finishTimes, reverse=True)]
exploredList, finishTimes, sccs = DFSLoop(adjacencyList, nodes)
print(sorted(sccs.values(), reverse=True)[0:10])
#print(adjacencyList)
#print(len(adjacencyList))
