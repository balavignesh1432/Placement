def trap(self, height: List[int]) -> int:
    # Intuition: Water collected at each position is min of maximum height to left and right
    # Minus the height of own position.
    # So compute preMax and postMax
    # Now compute the water collected at each position
    # TC: O(N), SC: O(N)
    
    n = len(height)
    preMax = []
    postMax = [0] * n

    currMax = height[0]
    for i in range(n):
        currMax = max(currMax, height[i])
        preMax.append(currMax)

    currMax = height[-1]
    for i in range(n - 1, -1, -1):
        currMax = max(currMax, height[i])
        postMax[i] = currMax

    water = 0
    for i in range(n):
        water += min(preMax[i], postMax[i]) - height[i]

    return water


    # Two pointers from beginning, Double Pass
    # Initialise left to  0, right to 1
    # incrment right until, it goes above height of left, while adding obstacles
    # Calculate, water capacity
    # Now reset left to right, reset obstacles to 0.
    # But this misses cases where left is high, 
    # but there is a direction change happening from up to low.
    # So to also include that case, run this again in reverse.
    # Since when left and right are equal height could be included in both, check for direction
    # TC: O(N), SC: O(1)
    res = 0
    def calcWater(direction):
        left = 0
        right = 1
        water = obs = 0
        while right < len(height):
            obs += height[right]
            if (direction == 0 and height[left] <= height[right]) or (direction == 1 and height[left] < height[right]):
                obs -= height[right]
                water += (min(height[right], height[left]) * (right - left - 1)) - obs
                left = right
                obs = 0
            right += 1
        return water
    res += calcWater(0)
    height.reverse()
    res += calcWater(1)
    return res