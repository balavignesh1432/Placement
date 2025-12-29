def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    # Brute Force:
    # For each temp, start from next until higher temp is found
    # If found, store the distance, if reached end, then 0
    # TC: O(N^2), SC: O(1)
    res = []
    for i in range(len(temperatures)):
        count = 1
        j = i + 1
        while j < len(temperatures):
            if temperatures[j] > temperatures[i]:
                break
            j += 1
            count += 1
        count = 0 if j == len(temperatures) else count
        res.append(count)
    return res


    # Mono Decreasing Stack:
    # Traverse from end, maintain stack in decreasing temperatures
    # For each temp, pop until higher temp is found,
    # If found, calculate distance
    # If stack empty, then distance is 0
    # Push currennt temperature and index to stack
    # TC: O(N), SC: O(N)
    res =  [0] * len(temperatures)
    stack = []
    for i in range(len(temperatures) - 1, -1, -1):
        while stack and stack[-1][0] <= temperatures[i]:
            temp, index = stack.pop()
        if stack:
            res[i] = stack[-1][1] - i 
        stack.append([temperatures[i], i])
    return res