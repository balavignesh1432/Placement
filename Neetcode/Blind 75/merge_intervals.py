def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    # TC: O(N), SC: O(1) only for storing result N
    # Intuition if sorted intervals, keep comparing last interval of result and current interval of list
    # Initially sort and add first interval to result
    # If current interval is totally above last interval just add current to result
    # If current interval is totally before last of res (newInterval added at start), pop and add current and then last interval of res back again
    # If not both the case, then overlapping interval, then obtain the values for merging intervals min and max,
    # Then pop the last element of res and add this overlap updated interval
    intervals.sort()
    res = []
    res.append(intervals[0])
    for i in range(1, len(intervals)):
        start, end = intervals[i][0], intervals[i][1]
        if start > res[-1][1]:
            res.append([start, end])
        elif end < res[-1][0]:
            last = res.pop()
            res.append([start, end])
            res.append(last)
        else:
            update = [min(res[-1][0], start), max(res[-1][1], end)]
            res.pop()
            res.append(update)
    return res