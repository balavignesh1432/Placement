def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    # Greedy: Main Intuition.
    # IMP: If starting from station S you run out of gas before reaching station i+1,
    # Then no station between S and i can be a valid start.
    # Find difference of gas and cost for each position
    # Total is < 0, that means not possible to start from any place so return -1
    # Now iterate in the diff array, if starting at an index, add to sum,
    # If sum drop below 0, then that can not be start, so reset sum and set start to i + 1
    # Because nothing from start to i can be a starting point
    # Because if so then summation from start to i would not have fallen below 0
    # So starting point is definitely towards the right
    # Also there exists only one unique solution according to question
    # TC: O(N), SC: O(N)
    diff = []
    for i in range(len(gas)):
        diff.append(gas[i] - cost[i])

    if sum(diff) < 0:
        return -1

    sumCount = 0
    start = 0
    for i in range(len(diff)):
        sumCount += diff[i]
        if sumCount < 0:
            sumCount = 0
            start = i + 1
    return start


    # Space optimised: Since array of diff is not needed and can be computed at runtime.
    # TC: O(N), SC: O(1)
    if sum(gas) - sum(cost) < 0:
            return -1
    sumCount = 0
    start = 0
    for i in range(len(gas)):
        sumCount += gas[i] - cost[i]
        if sumCount < 0:
            sumCount = 0
            start = i + 1
    return start