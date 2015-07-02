def mergesort(x):
    if len(x) < 2:
        return x
    halfLength = len(x)//2
    # get the left part of the input array
    left = x[:halfLength]
    # get the right part of the input array
    right = x[halfLength:]
    print("left: {0}, right: {1}".format(left, right))
    # sort left part of the input array
    sortedLeft = mergesort(left)
    # sort right part of the input array
    sortedRight = mergesort(right)
    print("sorted left: {0}, sorted right: {1}".format(left, right))
    # merge sorted left and right arrays
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
    print("merged {0}".format(merged))
    return merged

print(mergesort([1, 5, 3, 2, 4]))
