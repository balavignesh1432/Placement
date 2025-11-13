def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    # TC: O(N), SC: O(1) only for storing result N
    # Intuition keep comparing last interval of result and current interval of list
    # So, Add newInterval to result initially
    # If current interval is totally above last interval just add current to result
    # If current interval is totally before last of res (newInterval added at start), pop and add current and then last interval of res back again
    # If not both the case, then overlapping interval, then obtain the values for merging intervals min and max
    # Then pop the last element of res and add this overlap updated interval
    res = []
    res.append(newInterval)
    for i in range(len(intervals)):
        start, end = intervals[i][0], intervals[i][1]
        if end < res[-1][0]:    # Current interval has to come before
            last = res.pop()        
            res.append([start, end])
            res.append(last)
        elif start > res[-1][1]: # Current interval has to come after
            res.append([start,end]) 
        else:   # Overlapping Intervals
            update = [min(res[-1][0], start), max(res[-1][1], end)]
            res.pop()
            res.append(update)
    return res