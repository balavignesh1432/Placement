def maxArea(self, height: List[int]) -> int:
    # Brute Force: Calculate all possible areas
    # TC: O(N*2), SC: O(1)
    maxArea = 0
    for i in range(len(height)):
        for j in range(i, len(height)):
            area = min(height[j], height[i]) * (j - i)
            maxArea = max(area, maxArea)
    return maxArea

    # Two Pointer: Intuition, Start from where best area can be possible which is from ends,
    # This way easier to which pointer to move inward that could possibly give even more area
    # Here limiting factor is minimum of their heights.
    # So if we move the smaller pointer inwards, we can expect higher area if it has higher height.
    # We can be sure that moving the smaller pointer inward will not lose any cases, 
    # Because even at worst anything is even smaller, we already calculated the best area.
    # So safe to move smaller pointer inwards.
    # TC: O(N), SC: O(1)
    l = 0
    r = len(height) - 1
    maxArea = 0
    while l <= r:
        area = (r - l) * min(height[l], height[r])
        maxArea = max(maxArea, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return maxArea