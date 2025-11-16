def canAttendMeetings(self, intervals):
    # Brute: TC: O(N * 2), SC: O(1)
    # Check each interval with every other interval on right side
    # If overlap return False, if none return true
    for i in range(len(intervals)):
        start, end = intervals[i][0], intervals[i][1]
        for j in range(i + 1, len(intervals)):
            if intervals[j][0] >= end or intervals[j][1] <= start:  # Check No Overlap: if interval is completely before or after
                continue
            else:
                return False
    return True

    # Sorting: TC: O(N log N), SC: O(1)
    # Iterate from beginning, if interval start overlaps with previous end time, then not possible
    # If completed loop, return True
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][-1]:
            return False
    return True