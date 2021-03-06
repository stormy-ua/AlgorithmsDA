# import sys
# sys.setrecursionlimit(10100)

comparisons = 0
calls = 0
x = []

def swap(x, i, j):
    tmp = x[i]
    x[i] = x[j]
    x[j] = tmp

def choosePivot(x, l, r):
    return r
    # first = x[l]
    # last = x[r]
    # middle = x[(r + l)//2]
    # if (first < middle < last) or (last < middle < first):
    #     return (r + l)//2
    # elif (middle < first < last) or (last < first < middle) or (middle == first):
    #     return l
    # elif (first < last < middle) or (middle < last < first):
    #     return r

def partition(x, l, r, i):
    pivot = x[i]
    # put the pivot at the beginning of the array
    swap(x, l, i)
    i = l + 1
    for j in range(l + 1, r + 1):
        if x[j] < pivot:
            swap(x, j, i)
            i += 1
    swap(x, l, i - 1)
    return i - 1

def quicksort(x, l=0, r=None):
    # global calls
    # calls += 1
    #print(calls)
    # if array has length equal to 1 then no sorting needed
    if len(x) <= 1:
        return
    # calculate the rightmost index if it wasn't specified
    if r is None:
        r = len(x) - 1

    global comparisons
    if r > l:
        comparisons += r - l;

    # if subarray has 1 element then no sorting needed
    if r - l <= 0:
        return

    #print("sorting range: [{0}, {1}]".format(l, r))
    i = choosePivot(x, l, r)
    #print("chosen pivot: {0}".format(i))
    # partition and return the position of the pivot in the partitioned array
    i = partition(x, l, r, i)
    quicksort(x, l, i - 1)
    quicksort(x, i + 1, r)
    return


with open("QuickSort.txt") as f:
    array = [int(l) for l in f.readlines()]

#print(array)

#x = [3, 2, 5, 6, 1, 4, 9, 7, 0, 8, 10]
x = array
quicksort(x)
#print(x)
print(comparisons)

#162085
#164123
#155495
