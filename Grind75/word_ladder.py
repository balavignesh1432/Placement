def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    # BFS: For start word, at each position try all lower case characters
    # Only move to next word, if that word formed is in wordList (convert to set)
    # Since shortest distance to target word is needed, use BFS
    # Add beginning word to q, with distance as 1
    # Mark word visited by adding to set
    # Explore all characters for all index, and check word in word set and not already visited
    # Then add to q, with dist + 1
    # If target word reached return the distance, if not reachable 0 (At last)
    # TC: O(L^2 * N * 26), SC: O(L * N), where L is length of the string, N wordlist count
    # L * 26 for the loops, L for slicing.
    wordSet = set(wordList)
    q = deque()
    q.append([beginWord, 1])
    visited = set()
    target = endWord
    while q:
        word, d = q.popleft()
        if word == target:
            return d
        visited.add(word)
        for i in range(len(word)):
            for c in range(26):
                newWord = word[:i] + chr(c + 97) + word[i+1:]
                if newWord in wordSet and newWord not in visited: # Only move if in wordSet and not already visited
                    q.append([newWord, d + 1])
    return 0    