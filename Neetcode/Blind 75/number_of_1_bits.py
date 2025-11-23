# Intuition, just last bit has to be accessed, and should be added to counter if 1
# For getting last bit, either divide by 2 and remainder (Odd will have 1, even 0), 
# Or mask by and with 1, which has all bits except last bit as zero, if result is 1, then add
# For continously accessing last bit, bit shift by 1 place right side
# Keep repeating until number becomes 0
# TC: O(log n), 32 bits length for each unsigned number representation, SC: O(1) 
def hammingWeight(self, n: int) -> int:
    setBits = 0
    while n:    # If number becomes 0, no 1s will be there
        if n & 1:   # Or n%2 also works, but bitwise operator is slightly faster
            setBits += 1
        n = n >> 1  # Right shift by 1
    return setBits 

    # Slightly better, & with n-1, can be used to progressively only iterate from last, for bits set 1
    # Becomes 0 faster, if 1s are sparse
    setBits = 0
    while n:
        n = n & (n - 1)
        setBits += 1
    return setBits