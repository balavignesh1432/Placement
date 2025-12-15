def findMinArrowShots(self, points: List[List[int]]) -> int:
    # Since it effectively turns into overlapping intervals problem
    # But whenever there is overlap, update the last interval as that overlap only
    # Since it is width of balloon, only in the overlap portion, can arrow burst it
    # So sort the points, then if no overlap, reset last interval to current, increase counter
    # If overlap, then update the interval to only overlap portion
    # TC: O(N log N), SC: O(1)
    points.sort()
    last = points[0]
    count = 1
    for i in range(1, len(points)):
        start = points[i][0]
        end = points[i][1]
        if start > last[1]:
            count += 1
            last = [start, end]
        else:
            last = [start, min(end, last[1])]
    return count 