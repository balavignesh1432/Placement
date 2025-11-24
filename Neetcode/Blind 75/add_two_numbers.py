class Solution:
    # Perform Binary addition,
    # 1 1 should be 0, and carry 1
    # 0 0 should be 0, and carry 0
    # 1 0 or 0 1 should be 1, and carry 0
    # So basically xor carry, digit1 and digit2 for value
    # And update carry for next iteration
    # If results exceeds max possible positive integer, then number must be negative, so 2s complement needed.
    # Max positive integer is 2^32 - 1, which is represented as 0x7FFFFFFF (F is 8 1111, 7 is 0111)
    # If so, flip the bits, (XOR with 32 1s which is 0xFFFFFFFF)
    # ~x means -(x + 1), if x is positive, increments x puts -, if x is negative, adds 1, then puts -1
    # ~3 is -4, ~-4 is 3 
    # Flipping gives the complement of negative number in positive, now have to get negative complement using ~
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        mask = 0xFFFFFFFF   # XOR with 32 ones to flip all 32 bits
        max_int = 0x7FFFFFFF    # Max integer, all ones except left most
        for i in range(32):
            a_bit = (a >> i) & 1    # Get last digit of a
            b_bit = (b >> i) & 1    # Get last digit of b
            cur_bit = a_bit ^ b_bit ^ carry # Compute the value of added bits
            res |= (cur_bit << i)   # OR operator for storing bit, shift bit to be stored to appropriate position
            if a_bit & b_bit:       # If both bits 1, then carry will always be 1
                carry = 1
            else:                   # If either is 1, and carry is 1, then carry will be 1, otherwise 0
                carry = (a_bit | b_bit) & carry
        if res > max_int:    # If bigger than max positive integer, take 2s complement
            res = ~(res ^ mask)     
        return res