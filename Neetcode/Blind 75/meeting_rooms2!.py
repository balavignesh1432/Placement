def minMeetingRooms(self, start, end):
    # Sort the intervals based on start
    # Add 1st interval to first room, then iterate from 2nd interval
    # Check if start does not overlap with any of rooms last end time, if so interval to that room
    # If overlaps with all room, create new room and add that interval
    # TC: O(N^2), SC:O(N)
    intervals = [[s, e] for s,e in zip(start, end)]
    intervals.sort()
    res = []
    res.append([intervals[0]])
    for i in range(1, len(intervals)):
        start, end = intervals[i][0], intervals[i][1]
        newRoom = True
        for j in range(len(res)):
            if start >= res[j][-1][1]:
                res[j].append([start, end])
                newRoom = False
                break
        if newRoom:
            res.append([[start, end]])
    return len(res)
    
    # Heap - Intuition: After sorting intervals based on start, 
    # When checking if start of interval overlap , checking is from previous intervals minimum end time
    # If minimum end time is still not over, meaning start < min end, then overlap
    # If overlap add incoming interval's end into some memory
    # If incoming interval's start >= min end time, that means that interval is over, no overlap, and need to be popped out
    # Keep popping until the condition, or the memory is empty, memory represents overlapping intervals
    # The push the incoming end into memory, 
    # Since only minimum end time is needed, using Heap it is efficient as each operation is O(log N).
    # TC: O(N log N), SC: O(N) 
    intervals = [[s, e] for s,e in zip(start, end)]
    intervals.sort()
    minheap = []
    heapq.heappush(minheap, intervals[0][1])
    res = 0
    for i in range(1, len(intervals)):
        start, end = intervals[i][0], intervals[i][1]
        if start < minheap[0]:  # Overlap, as interval still not over and one is starting
            heapq.heappush(minheap, end)
        else:
            while minheap and start >= minheap[0]:  #No Overlap, interval over before this one starting so remove that end from overlap         
                heapq.heappop(minheap)
            heapq.heappush(minheap, end)
        res = max(res, len(minheap))
    return res
    
    
    # Intuition: Think graph, Problem is basically maximum overlap width at any given time
    # Sort start and end independently, use two pointers from starts
    # Now lowest value in end, meetings have to start after it to avoid overlap
    # So from lowest value in start, while start < end time, increment start pointer, and width value
    # Since there is overlap, increase width, and keep track of maximum
    # Then while end <= start, increment end pointer, and decrese width value, 
    # as this means meetings are only after end is finished, so overlap width is reduced
    # TC: O(N log N), SC: O(1), Ignoring space for sorting N
    start.sort()
    end.sort()
    overlapWidth = res = 0
    i = j = 0
    while i < len(start) and j < len(end):
        while i < len(start) and start[i] < end[j]:
            overlapWidth += 1
            i += 1
            res = max(res, overlapWidth)
        while i < len(start) and j < len(end) and start[i] >= end[j]:
            overlapWidth -= 1
            j += 1
    return res

    