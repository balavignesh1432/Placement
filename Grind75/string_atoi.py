def myAtoi(self, s: str) -> int:
    # Use pointer to move preceding spaces
    # Then take the sign and move one place
    # Then skip all preceeding zeroes
    # Then iterate until non digit
    # Then convert to number
    # Check if greater than INT_MAX,
    # If so depending on sing, if positive, then resort to INT_MAX (0x7FFFFFFF)
    # Else, -0x80000000 (Only 1 digit 1 rest all 0s)
    # TC: O(N), SC: O(1)
    res = 0
    pos = 0
    sign = 0
    while pos < len(s) and s[pos] == " ":
        pos += 1
    if pos < len(s) and (s[pos] == "-" or s[pos] == "+"):
        if s[pos] == "-":
            sign = 1
        pos += 1
    while pos < len(s) and s[pos] == "0":
        pos += 1
    start = pos
    while pos < len(s) and s[pos].isdigit():
        pos += 1
    if pos > start:
        res = int(s[start:pos])
        if res > 0x7FFFFFFF:
            res = 0x80000000 if sign else 0x7FFFFFFF
        res = -res if sign else res
    return res