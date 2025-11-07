def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Brute - TC O(N^2), SC - O(1)
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    # Sorting and Two pointers from ends
    # Technique to store index and element in array to not lose track when sorting
    # TC - O(N log N), SC - O(N) 
    copy = []
    for i in range(len(nums)):
        copy.append([nums[i], i])
    copy.sort()
    i = 0
    j = len(nums) - 1
    while i < j:
        if copy[i][0] + copy[j][0] == target:
            return [copy[i][1], copy[j][1]]
        elif copy[i][0] + copy[j][0] < target:
            i += 1
        else:
            j -= 1
    
    # Using HashMap to search for other number that could add to target
    # In single pass, store visited in map, check if necessary in visited
    # Since index is needed HashMap is needed instead of HashSet
    hashMap = {}
    for i in range(len(nums)):
        if target - nums[i] in hashMap:
            return [i, hashMap[target - nums[i]]]
        else:
            hashMap[nums[i]] = i