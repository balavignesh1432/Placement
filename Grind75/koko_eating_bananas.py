def minEatingSpeed(self, piles: List[int], h: int) -> int:
    # Brute Force: 
    # Check lowest speed 1 to max of pile
    # IF possible to eat before h, return as it the lowest speed answer
    # TC: O(N * M), SC: O(1)
    low = 1
    high = max(piles)
    speed = low
    while speed <= high:
        hour = 0
        for i in range(len(piles)):
            hour += (piles[i] // speed)
            if piles[i] % speed:
                hour += 1
        if hour <= h:
            return speed
        speed += 1
    return speed
    # Binary Search on Answer
    # Trying every value from 1 to highest pile size, since even if speed greater than pile size
    # It can take 1 hour
    # Use binary search on the answer
    # Check if it can be the answer
    # Divide pile size by speed to get hours needed, it could be remainder if so add 1 more hour
    # If can be done within h, decrement speed, move right to mid, as it can be answer dont skip
    # If cannot be done move left to mid + 1, as mid cannot be answer
    # When both pointer meet, that is the answer, so return either of them at the end
    # TC: O(N Log M), SC: O(1)
    # Where N is the length of the list, M is the max banana in a pile
    right = max(piles)
    left = 1
    while left < right:
        mid = (left + right) // 2
        hour = 0
        for i in range(len(piles)):
            hour += (piles[i] // mid)
            if piles[i] % mid:
                hour += 1
        if hour <= h:
            right = mid
        else:
            left = mid + 1
    return right