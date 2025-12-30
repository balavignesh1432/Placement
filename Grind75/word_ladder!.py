def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    # BFS: For start word, at each position try all lower case characters
    # Only move to next word, if that word formed is in wordList (convert to set)
    # Since shortest distance to target word is needed, use BFS
    # Add beginning word to q, with distance as 1, as beginWord is counted in transformation
    # To avoid visiting same word again, remove from wordSet when added to q
    # Explore all characters for all index, and check word in word set
    # Then add to q, with dist + 1
    # If target word reached return the distance, if not reachable 0 (At last)
    # TC: O(L^2 * N * 26), SC: O(L * N), where L is length of the string, N wordlist count
    # L * 26 for the loops, L for slicing.
    wordSet = set(wordList)
    q = deque()
    q.append([beginWord, 1])
    if beginWord in wordSet:
        wordSet.remove(beginWord)
    if endWord not in wordSet:
        return 0
    while q:
        word, d = q.popleft()
        if word == target:
            return d
        for i in range(len(word)):
            for c in range(26):
                newWord = word[:i] + chr(c + 97) + word[i+1:]
                if newWord in wordSet:               # Only move if in wordSet
                    q.append([newWord, d + 1])
                    wordSet.remove(newWord)          # Remove to avoid revisiting
    return 0 