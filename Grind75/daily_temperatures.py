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


    # Stack:
    # Check if temp is greater than top element in stack
    # If so, pop that element, update top element's result by computing distance
    # Keep repeating this until temp is smaller than top or stack is empty
    # Then push the current element to stack
    # TC: O(N), SC: O(N)
    res =  [0] * len(temperatures)
    stack = []
    for i in range(len(temperatures)):
        while stack and stack[-1][0] < temperatures[i]:
            temp, index = stack.pop()
            res[index] = i - index
        stack.append([temperatures[i], i])
    return res