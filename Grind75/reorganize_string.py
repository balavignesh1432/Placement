def reorganizeString(self, s: str) -> str:
    # Greedily pick the most frequent character available
    # Use a max-heap to always get the most frequent character
    # If the most frequent character is same as the last appended character
    # pick the next most frequent character
    # If no other character is available, return "", as it's not possible to reorganize
    # Modify the count and reinsert into the heap if still available
    # Time Complexity: O(N log 26) where N is length of string and K is number of unique characters
    # Space Complexity: O(26) for the count dictionary and max-heap
    # But K <= 26 for lowercase English letters, so O(1) space effectively
    count = {}
    maxHeap = []
    res = []
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in count:
        heappush(maxHeap, [-count[c], c])
    while maxHeap:
        count, c = heappop(maxHeap)         # Get the most frequent character
        if len(res) and c == res[-1]:       # If same as last appended character
            if not maxHeap:                 # No other character to use
                return ""
            store = [count, c]              # Store the current character
            count, c = heappop(maxHeap)     # Get the next most frequent character
            heappush(maxHeap, store)        # Push back the stored character
        res.append(c)                       # Append the chosen character
        count += 1                          # Decrease the count of the chosen character
        if count < 0:                       # If still available, 
            heappush(maxHeap, [count, c])   # Reinsert into the heap
    return "".join(res)