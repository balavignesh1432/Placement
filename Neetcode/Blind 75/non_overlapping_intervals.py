def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    # Sorting and Removing inteerval with farther tail
    # After sorting, put the 1st interval in new list
    # Then from second, keep comparing to last element of new list,
    # If no overlap, add to res list
    # If overlap, then check which one has longer tail, 
    # If incoming has longer, then skip adding to res list
    # If res end has longer tail, then pop it and add incoming interval to res
    # NOTE: Bigger end interval is one to be removed, not the larger sized interval
    # Think case when left is bigger, but right is smaller than it, but has many overlapping intervals beneath it
    # TC: O(N log N), SC: O(N) 
    intervals.sort()
    res = []
    res.append(intervals[0])
    for i in range(1, len(intervals)):
        start, end = intervals[i][0], intervals[i][1]
        if start >= res[-1][1]:
            res.append([start, end])
        else:
            if end < res[-1][1]:
                res.pop()
                res.append([start, end])
    return len(intervals) - len(res)


    # Space Optimized Version, since only end value of lastly added is needed, and the size of res.
    # Instead of storing intervals, only last added value and size of it will be kept track.
    # Depending on whether we would pop or just add the interval, size will be +1 or same.
    # And, new end will be determined whether incoming one's or existing one's.
    # TC: O(N log N), SC: O(1) 
    intervals.sort()
    prevEnd = intervals[0][1]
    size = 1
    for i in range(1, len(intervals)):
        start, end = intervals[i][0], intervals[i][1]
        if start >= prevEnd:
            prevEnd = end
            size += 1
        else:
            if end < prevEnd:
                prevEnd = end
    return len(intervals) - size