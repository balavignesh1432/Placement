#Merge Sort - O(N*log N) - Space O(N) - Stable
#Height of tree is log N, and at a level worst case merge takes N.
nums = [5,1,1,2,0,0]

# Just using indices for recursion and partitioning
def mergeSort(start, end):
    if start == end: #Base case when only one element return array of that element alone
        return [nums[start]]
    
    # Split Point Logic
    mid = (start + end) // 2 
    
    # Partition Logic - Array is returned
    left = mergeSort(start, mid)       
    right = mergeSort(mid + 1, end)

    # Needs auxillary memory for merge
    result = []
    
    # Use two pointers for merging the sorted arrays into new array
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])        
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Handling when one is exhausted before the other.
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    
    # Returning merged array
    return result
print(mergeSort(0, len(nums) - 1))