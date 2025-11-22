# Brute Force: Perform DFS for each cell, and for each word
# Pass words index, and the position of current pointer to compare 
# Add to path set, Call with neighbours, and increment current pointer
# Base case, out of bounds or already in path, return False
# If end of word reached, add word to list, return True
# If any of the calls return True, return True, as word is Found and no more dfs needed
# Remove from path set before returning
# Use found array to keep track of words that are found, index of found words in words list
# If dfs call return True at the end, then mark the word as found, only call dfs for not found words
# TC: O(M * N * W * 4^L) where L is avg. length of word, SC: O(L + W), depth of dfs is L
def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    res = []
    found = [False] * len(words)
    path = set()
    def dfs(row, col, word, pos):
        if pos == len(words[word]):
            res.append(words[word])
            return True
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or (row, col) in path:
            return False
        path.add((row, col))
        if words[word][pos] == board[row][col]:
            for rd, cd in directions:
                if dfs(row + rd, col + cd, word, pos + 1):
                    path.remove((row, col))
                    return True
        path.remove((row, col))
        return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            for k in range(len(words)):
                if not found[k] and dfs(i, j, k, 0):
                    found[k] = True
    return res


# Instead of going through list of words every time for dfs call,
# If words are stored in trie, then can be moved down in trie during dfs,
# when there is letter available at that depth.
# If end of word reached, then add to result, but still call if there is letter available at the depth
# Since same prefix can be there like aa, aaa.
# Use path set to not come back along the same path
# Check endword before calling next, to avoid adding 3 more times in each direction, 
# (Since Trie end is only marked at the next level)
# TC: O(M * N * 4^L + W *L), W L for building Trie, SC: O(W*L + L) For Building and Stack depth
class Trie:
    def __init__(self):
        self.charList = [None] * 26
        self.endOfWord = False

    def addWord(self, word):
        head = self
        for c in word:
            index = ord(c) - ord('a')
            if not head.charList[index]:
                head.charList[index] = Trie()            
            head = head.charList[index]
        head.endOfWord = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordsTrie = Trie()
        for word in words:
            wordsTrie.addWord(word)
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        res = set()
        path = set()
        def dfs(row, col, word, wordsTrie):
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or (row, col) in path:
                return
            index = ord(board[row][col]) - ord('a') 
            if wordsTrie.charList[index]:
                path.add((row, col))
                wordsTrie = wordsTrie.charList[index]   
                word = word + board[row][col]
                if wordsTrie.endOfWord:
                    res.add(word)
                for rd, cd in directions:
                    dfs(row + rd, col + cd, word, wordsTrie)
                path.remove((row, col))
                return 
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, "", wordsTrie)
        return list(res)



# Slight Optimisation, to avoid already found word, and if no other word
# that starts with that letter is yet to be found
# When adding words to trie, add to map with key as first letter and value is set of words starting with that letter
# When adding word to res, remove that word from map's value set,
# Only call dfs for cells which starting letter has still words to be found.
# Gets Run Time from 8.5s to 4.5s, many cases where same words is available in grid multiple places
class Trie:
    def __init__(self):
        self.charList = [None] * 26
        self.endOfWord = False
    def addWord(self, word):
        head = self
        for c in word:
            index = ord(c) - ord('a')
            if not head.charList[index]:
                head.charList[index] = Trie()            
            head = head.charList[index]
        head.endOfWord = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordsTrie = Trie()
        notFound = {}
        for word in words:
            wordsTrie.addWord(word)
            if word[0] not in notFound:
                notFound[word[0]] = set()
            notFound[word[0]].add(word)
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        res = set()
        path = set()
        def dfs(row, col, word, wordsTrie):
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or (row, col) in path:
                return
            index = ord(board[row][col]) - ord('a') 
            if wordsTrie.charList[index]:
                path.add((row, col))
                wordsTrie = wordsTrie.charList[index]   # Check end before calling to avoid adding 3 more times in each direction
                word = word + board[row][col]
                if wordsTrie.endOfWord:
                    res.add(word)
                    if word in notFound[word[0]]:
                        notFound[word[0]].remove(word)
                for rd, cd in directions:
                    dfs(row + rd, col + cd, word, wordsTrie)
                path.remove((row, col))
                return 
        for i in range(len(board)):
            for j in range(len(board[0])):
                start = board[i][j][0]
                if start in notFound and len(notFound[start]):
                    dfs(i, j, "", wordsTrie)
        return list(res)