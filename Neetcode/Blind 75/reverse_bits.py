def reverseBits(self, n: int) -> int:
    # Get the last bit, put that in another variable,
    # Move n to right, move res to left taking each bit,
    # Last bit using & with 1, 
    # For storing, last bit, using or operator with 0, and shift by left to store it
    # Have to perform 31 times, as signed integer
    # Can not run for log n times, as 0 bits are also needed, so complete shift is needed
    res = 0
    for _ in range(31): 
        res = res | (n & 1) 
        n = n >> 1
        res = res << 1
    return res