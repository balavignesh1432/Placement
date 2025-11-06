nums = [5,1,1,2,0,0]

# Exchange Sort 0(N^2) - Not Stable
# Simply sending smallest to the beginning
# Achieved through swapping with beginning if found smaller element in its right window.
# Window shrinks from the beginning.
def exchangeSort():
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

# Selection Sort - O(N^2) - Not Stable
# Most intuitive, find minimum in each step and swap with lowest position of that iteration
def selectionSort():
    for i in range(len(nums)):
        mini = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[mini]:
                mini = j
        nums[i], nums[mini] = nums[mini], nums[i]
    return nums

# Bubble Sort - O(N^2) - Stable (As swapping is only between adjacent items)
# Sending Heaviest to Last by adjacent swapping
# Window shrinks from the end side.
def bubbleSort():
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

# Insertion Sort - O(N^2) - Stable (As swapping is only between adjacent items)
# For Each position insert the element at that position at right place within the window until that position starting from the beginning
# Insertion enabled through progressive adjacent swapping with previous elements
def insertionSort(): 
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]: 
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums

# Space Complexity - O(1) for all N^2 Sorting Algos

# Use this Case for Stability Check
# nums = [(3, 'A'), (3, 'B'), (2, 'C')]