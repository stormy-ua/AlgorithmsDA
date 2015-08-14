from heapq import *

stream = []

with open("Median.txt") as f:
    for l in f.readlines():
        stream.append(int(l))

#stream = [3, 2, 1, 7, 5, 9, 4]

lowHeap = []
highHeap = []

def ingestValue(lowHeap, highHeap, value):
    lowLength = len(lowHeap)
    highLength = len(highHeap)
    lowHeapMax = nlargest(1, lowHeap)[0] if lowLength > 0 else None
    highHeapMin = highHeap[0] if highLength > 0 else None

    if lowHeapMax is None or value <= lowHeapMax:
        heappush(lowHeap, value)
        lowLength += 1
    else:
        heappush(highHeap, value)
        highLength += 1

    # re-balancing
    if lowLength - highLength > 1:
        lowHeapLargest = nlargest(1, lowHeap)[0]
        lowHeap.remove(lowHeapLargest)
        heappush(highHeap, lowHeapLargest)
        lowLength -= 1
        highLength += 1
    elif highLength - lowLength > 1:
        highHeapSmallest = heappop(highHeap)
        heappush(lowHeap, highHeapSmallest)
        lowLength += 1
        highLength -= 1

    if lowLength >= highLength or highHeapMin is None:
        return nlargest(1, lowHeap)[0]
    else:
        return highHeap[0]

sum = 0

for value in stream:
    median = ingestValue(lowHeap, highHeap, value)
    sum += median
    print("{0}:{1}".format(sum, median))

print(sum % 10000)
