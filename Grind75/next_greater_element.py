def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # Brute Force would be check nearest greater from each position
    # TC: O(M * N), SC: O(1)

    # Using Monotonic Stack
    # Since if a number is bigger than right elements, then those right elements are not needed
    # when considering nge for left elemets, so we can pop them
    # So from last maintain Mono Decreasing stack
    # If element smaller than top, top is nge, and append to stack
    # If element is larger, all the smaller elements are not needed, so keep popping
    # If stack becomes, then nge is -1, and append to stack
    # Put in Hasmap for nge, which could be used when iterating nums1
    # TC: O(M + N), SC: O(N)
    stack = []
    nge = {}
    for i in range(len(nums2) - 1, -1, -1):
        while stack and nums2[i] > stack[-1]:
            stack.pop()
        nge[nums2[i]] = -1 if not stack else stack[-1]
        stack.append(nums2[i])
    return [nge[num] for num in nums1]