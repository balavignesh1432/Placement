def reverseBits(self, n: int) -> int:
    # Get the last bit, put that in another variable,
    # Move n to right, move res to left taking each bit,
    # Last bit using & with 1, 
    # For storing, last bit, using or operator with 0, and shift by left to store it
    # Can not run for log n times, as 0 bits are also needed, so complete shift is needed
    # At last shift res right by 1, to undo last shift which was needed to store bit coming in next iteration
    # Since it is last iteration, there wont be next bit
    # TC: O(32), SC: O(1)
    res = 0
    for _ in range(32): 
        res = res | (n & 1) 
        n = n >> 1
        res = res << 1  # Making space to store bit in next iteration
    return res >> 1