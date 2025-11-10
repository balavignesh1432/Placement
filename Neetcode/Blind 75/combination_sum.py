        
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    # All elements are distinct, so no case for duplicates
    # At each step, two option to take or not take (only increment index)
    # Since same element can be taken multiple times, do not move index when taking
    # For ending, sum should not exceed, and index should not be out of bounds
    # If sum matches target, add the list to result
    # TC: O(2^target/minimum), SC: O(target/minimum) Since same element can be taken, 
    # target and minimum (Lowest could be 1 which is the worst possible: target) defines the performance
    res = []
    def helper(index, comb, combSum):
        if index < len(candidates) and combSum <= target:
            if combSum == target:
                res.append(comb.copy()) # Since list is mutable, will be modified when pop, so take a copy
                return  # No more calling, since target already reached, elements are non zero
            comb.append(candidates[index])  # Avoid list + operator, as creates new copy for each call
            take = helper(index, comb, combSum + candidates[index])
            comb.pop() 
            notTake = helper(index + 1, comb, combSum)
    helper(0, [], 0)
    return res