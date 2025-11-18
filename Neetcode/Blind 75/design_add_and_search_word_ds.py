# Brute: Implementation using basic array
class WordDictionary:
    # SC: O(N * M), N: No.of words and M: Average Length of word
    def __init__(self):
        self.store = []

    # TC: O(1)
    def addWord(self, word: str) -> None:
        self.store.append(word)

    # TC: O(N * M), N: No.of words and M: Average Length of word
    def search(self, word: str) -> bool:
        for w in self.store:    # For Each word in store list
            if len(w) != len(word):
                continue
            i = 0
            while i < len(w):
                if w[i] == word[i] or word[i] == '.': # If both character of word, list word same increment
                    i += 1
                else:           # If mismatch, exit prematurely
                    break
            if i == len(w):
                return True
        return False

# Implementation using Trie, Better Search time for tradeoff with Add time
# Ususally preferred for searching words (Only limited set of characters)
class WordDictionary:
    # SC: O(N + T), where T is no.of.trie nodes, N is word length
    def __init__(self):
        self.charList = [None] * 26
        self.endOfWord = False

    # Get the root at the start,
    # Check if for the index, in the charList, whether a link is available or not.
    # If available go to that node with next letter.
    # Otherwise create a node, and make the link, and then proceed with next letter.
    # TC: O(N)
    def addWord(self, word: str) -> None:
        root = self
        for letter in word: # For each letter
            index = ord(letter) - ord('a')  # Get corresponding position for that letter
            if not root.charList[index]:    # If letter not present at that position, create node
                root.charList[index] = WordDictionary()
            root = root.charList[index]     # Update node for next letter
        root.endOfWord = True   # Set end Flag true, after inserting the word

    # TC: O(N), Since only 2 wild characters
    def search(self, word: str) -> bool:
        root = self
        # For each letter, check if there is a corresponding link for that index
        # If so call with that node and next letter
        # If not existing link for that index of letter, return False
        # If wild character, then check every index of the current node,
        # If link exists, then call with that node, and next letter
        # If one of the calls, returns True, return True, Otherwise return False
        # Base Case: If end of word reached, check if end flag is true for the node
        def helper(node, pos):
            if pos == len(word):
                return node.endOfWord
            if word[pos] != ".":
                index = ord(word[pos]) - ord('a')
                if not node.charList[index]:
                    return False
                return helper(node.charList[index], pos + 1)
            else:
                for i in range(26):
                    if node.charList[i] and helper(node.charList[i], pos + 1):
                        return True
                return False
        # Needed to be recursive, as depending on whether lowercase or ".", different methods
        # Call initially with root, and 1st letter
        return helper(root, 0)