def maxProduct(self, nums: List[int]) -> int:
    # Brute Force
    # For every subarray, compute product
    # Return the maximum product
    # TC: O(N*2), SC: O(1)
    maxProd = nums[0]
    for i in range(len(nums)):
        prod = 1
        for j in range(i, len(nums)):
            prod *= nums[j]
            maxProd = max(maxProd, prod)
    return maxProd

    # Observations: Max of Prefix and Suffix Products
    # 1. If all are positive numbers, then product of everything is answer
    # 2. If all are negative numbers, then it can be odd or even
    # 3. If even, then same as observation 1
    # 4. If odd, then except a negative number if we look at prefix and suffix products,
    # Those will contain maximum products, like in atleast one case,
    # it will split into even negatives inside prefix, and even negatives inside suffix.
    # So basically prefix product and suffix product, and the maximum will be the result.
    # So just compute prefix product and suffix product, and return the maximum found.
    # For observation 1 and 3, the last value of prefix or suffix will be the answer (which is maximum)
    # For observation 4, at any point during computation of prefix or suffix prod 
    # it will have done so by excluding that negative, and splitting into even negatives which would have given rise to maximum
    # 5. So the problem becomes finding prefixprod and suffixprod and returning maximum.
    # 6. What if zero is encountered, then prod becomes 0, for next iteration reset to 1
    # 7. Like splitting into segments without zero, and computing prefix and suffix prod.
    # TC: O(N), SC: O(1)
    prefixProd = suffixProd = 1
    maxProd = nums[0]   # Intialise with first element
    for i in range(len(nums)):
        prefixProd *= nums[i]
        suffixProd *= nums[(len(nums) - 1) - i]
        maxProd = max(maxProd, prefixProd, suffixProd)  # Calculate max before modifying to include 0 in answer
        # If products become 0, reset to 1 for starting from next iteration
        prefixProd = prefixProd or 1
        suffixProd = suffixProd or 1
    return maxProd