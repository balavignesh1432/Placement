def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    # To remove duplicates, sort
    # For not take case, move to distinct element, by moving the index pointer
    # Since sorted easier to perform this
    # Base case if taget reached, add to res 
    # If index valid, or sum is less than target only then move forward
    # Since all are positive elements.
    # TC: O(n∗2^n), SC: O(n) 
    res = []
    candidates.sort()
    def helper(index, comb, total):
        if total == target:
            res.append(comb.copy())
            return res
        if total > target or index == len(candidates):
            return
        comb.append(candidates[index])
        helper(index + 1, comb, total + candidates[index])
        comb.pop()
        while index < len(candidates) - 1 and candidates[index] == candidates[index + 1]:
            index += 1
        helper(index + 1, comb, total)
    helper(0, [], 0)
    return res