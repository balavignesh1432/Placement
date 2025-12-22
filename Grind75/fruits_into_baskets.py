def totalFruit(self, fruits: List[int]) -> int:
    # Sliding Window
    # Effectively turns into largets window with only two types of fruits
    # Use map to store fruits in window with count
    # When size exceeds 2, increment left and decrease count of left
    # When becomes 0, delete from map
    # Caluculate length, and keep track of max Length
    # TC: O(N), SC: O(1)
    pos = {}
    left = 0
    res = 0

    for i in range(len(fruits)):
        pos[fruits[i]] = pos.get(fruits[i], 0) + 1
        while len(pos) > 2:
            pos[fruits[left]] -= 1
            if pos[fruits[left]] == 0:
                del pos[fruits[left]]
            left += 1
        res = max(res, i - left + 1)

    return res