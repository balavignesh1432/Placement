nums = [5,1,1,2,0,0]

# Intuition is finding the correct position for pivot element
# Elements to left of pivot is smaller, right of it is bigger
# Pick any element(first, last, middle, random) as pivot
# Finding the place for it can be achieved through two pointers from ends

def quickSort(start, end):
    # Only if valid window and size is atleast 2
    if start < end: 
        pivot = start
        # Use two pointers from ends
        i = start
        j = end
        # Only when the pointers have not crossed
        while i < j:
            # Finding first position that is bigger than pivot from left
            while i <= end and nums[i] <= nums[pivot]:
                i += 1
            # Finding first position that is smaller than pivot from right
            while j >= start + 1 and nums[j] > nums[pivot]:
                j -= 1
            # Now these are the two elements that are incorrectly placed, so swap them
            # If pointers not crossed, then swap (If already crossed then work is only to place the pivot)
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        # j pointer points to position where pivot has to be placed
        nums[start], nums[j] = nums[j], nums[start]
        
        # Now Fix other two partitions
        quickSort(start, j - 1)
        quickSort(j + 1, end)
        
        # Nothing is return as sorting is performed on the input itself. In Place.
        return

quickSort(0, len(nums) - 1)
print(nums)

# Time Complexity - O(NlogN) - Average and Best; O(N^2) - Worst
# Height of tree can be N, when already sorted or reverse, 
# then partition will not be two halves [One element, and Rest of array].
# Space Complexity - O(1) In Place (Ignoring Call Stack)