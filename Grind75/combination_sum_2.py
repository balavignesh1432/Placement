def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    # Backtracking: Take and Not Take
    # To remove duplicates, sort
    # For not take case, move to distinct element, by moving the index pointer
    # Since sorted easier to perform this
    # Base case if taget reached, add to res
    # If index valid, or sum is less than target (Since all are positive elements) only then move forward 
    # TC: O(N ∗ 2^N), SC: O(N * 2^N) 
    # Since 2^N decisions/combinations and N to store each combination.
    res = []
    candidates.sort()
    def helper(index, comb, total):
        if total == target:
            res.append(comb.copy())
            return res
        if total > target or index == len(candidates):
            return
        comb.append(candidates[index])
        helper(index + 1, comb, total + candidates[index])  # Take
        comb.pop()
        while index < len(candidates) - 1 and candidates[index] == candidates[index + 1]: # Move to next distinct
            index += 1
        index += 1
        helper(index, comb, total)          # Not Take
    helper(0, [], 0)    
    return res