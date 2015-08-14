import bisect

numbers = set()

with open("2sum.txt") as f:
    for l in f.readlines():
        numbers.add(int(l))

sortedNumbers = list(numbers)
sortedNumbers.sort()

def get2sumTargets(minValue=-10000, maxValue=10000):
    value = minValue
    while value <= maxValue:
        yield value
        value += 1

def has2sum(numbers, t):
    # ymin = t - sortedNumbers[-1]
    # ymax = t - sortedNumbers[0]
    # low = bisect.bisect_left(sortedNumbers, ymin)
    # high = bisect.bisect_right(sortedNumbers, ymax)
    for x in numbers:
        y = t - x
        if y == x:
            continue
        if y in numbers:
            return 1
    return 0

t = 0
result = 0

for t in get2sumTargets():
    result += has2sum(numbers, t)
    print("{0}: {1}".format(t, result))

print(result)

#427 - result