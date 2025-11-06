# Key is hashed to obtain address, and value is stored
# Best and Average case TC O(1) for Search key, Write, Read values 
# Ex: Hash Function Division Method - Mod 10, to get the digit, there may be collision.
# Worst case, due to Chaining TC O(N), where N is the size of the hash map.

def countFrequencies(self, nums):
    # Manually counting frequencies of each unique element using another loop
    # Maintain another array to check if that index is already visited
    visited = [False] * len(nums)
    res = []
    for i in range(len(nums)):
        if visited[i]:  # Only if count not already calculated
            continue
        count = 1
        for j in range(i + 1, len(nums)):   # Just iterate to right side, as left already visited.
            if nums[j] == nums[i]: 
                count += 1
                visited[j] = True   # Update visited array
        res.append([nums[i], count])
    # TC - O(N * 2), SC - O(N)
    
    # Using Map, TC: O(N), SC: O(N)
    hashMap = {}
    for n in nums:
        if n not in hashMap:
            hashMap[n] = 1
        else:
            hashMap[n] += 1
    
    return [[k, v] for k, v in hashMap.items()]


# Highest and Lowest Frequeny elements
def getFrequencies(v: List[int]) -> List[int]: 
    # Brute force - Count frequency of each item like earlier using two loops.
    # Then find the smallest and largest. 
    # TC - O(N^2), SC - O(N)
    hashMap = {}
    for item in v:
        if item not in hashMap:
            hashMap[item] = 1
        else:
            hashMap[item] += 1
    
    # Find the highest and lowest frequency values
    maxf = max(hashMap.values())
    minf = min(hashMap.values())
    mink = maxk = max(v) + 1    # For picking smallest key in case of multiple candidates.
    
    # Find which item corresponds to those values
    for item in hashMap:
        if hashMap[item] == minf and item < mink:
            mink = item
        if hashMap[item] == maxf and item < maxk:
            maxk = item
    return [maxk, mink]

    # TC - O(N), SC - O(N)
