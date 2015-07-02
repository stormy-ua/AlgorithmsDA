def countinv(x):
    if len(x) < 2:
        return [x, 0]
    if len(x) < 3:
        return [x, 1] if x[0] > x[1] else [x, 0]
    halfLength = len(x)//2
    # get the left part of the input array
    left = x[:halfLength]
    # get the right part of the input array
    right = x[halfLength:]
    print("left: {0}, right: {1}".format(left, right))
    sortedLeft, invCountLeft = countinv(left)
    sortedRight, invCountRight = countinv(right)
    print("left: {0}, right: {1}".format([sortedLeft, invCountLeft], [sortedRight, invCountRight]))
    invCountSplit = 0
    merged = []
    i = 0
    j = 0
    for k in range(len(x)):
        if i >= len(sortedLeft):
            merged.append(sortedRight[j])
            j += 1
        elif j >= len(sortedRight):
            merged.append(sortedLeft[i])
            i += 1
        elif sortedLeft[i] <= sortedRight[j]:
            merged.append(sortedLeft[i])
            i += 1
        else:
            merged.append(sortedRight[j])
            j += 1
            invCountSplit += len(sortedLeft) - i
    print("merged {0}".format(merged))
    return [merged, invCountLeft + invCountRight + invCountSplit]

print(countinv([1, 3, 5, 2, 4, 6]))
#print(countinv([1, 2, 3, 4, 5, 6]))
#print(countinv([1, 2, 4, 3, 5, 6]))