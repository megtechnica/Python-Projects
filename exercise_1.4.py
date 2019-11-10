import bisect

def smaller_counts_naive(lst):
    result = []
    for i, num in enumerate(lst):
        count = sum(val < num for val in lst[i + 1:])
        result.append(count)

    return result

def smaller_counts(lst):
    result = []
    seen = []

    for num in reversed(lst):
        i = bisect.bisect_left(seen, num)
        result.append(i)
        bisect.insort(seen, num)

    return list(reversed(result))
