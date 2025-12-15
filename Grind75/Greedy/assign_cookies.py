def findContentChildren(self, g: List[int], s: List[int]) -> int:
    # Since child with smallest necessity has to be satisfied first to achieve higher count
    # Sort child, as well as cookies so that two pointers could be used
    # If satisfied, move both pointers, incrementing count
    # Or only move cookie pointer
    # TC: O(M log M + N log N), SC: O(1)
    g.sort()
    s.sort()
    i = 0
    j = 0
    count = 0
    while i < len(g) and j < len(s):
        if g[i] <= s[j]:
            count += 1
            i += 1
        j += 1
    return count