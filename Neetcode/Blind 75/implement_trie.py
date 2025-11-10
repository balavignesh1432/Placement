# TC: O(N), SC: O(H) Height of trie (H * 26)
# Important Things:
# Since multiple words share same path, flag needed for every node if word ended there
# During insertion, check if already the letter is inserted (shared prefix)
# If so do not create node, just go to the node pointed at that index
# For search word, at the end check is endofword flag true, not needed for startswith
# If index is None for the Node during search and startswith then that word is not there
class Trie:
    def __init__(self): 
        # Root node, everything None
        self.charList = [None] * 26
        self.endOfWord = False

    def insert(self, word: str) -> None:
        root = self # Get the root node
        for letter in word:
            index = ord(letter) - ord('a')
            if root.charList[index] == None:    # Check if already inserted that letter
                node = Trie()   # Create node
                root.charList[index] = node
                root = node # Update for next letter
            else:   # If inserted already, go to that node for next letter
                root = root.charList[index] 
        root.endOfWord = True # End of word is reached, so for last letter set true
    def search(self, word: str) -> bool:
        root = self
        for letter in word:
            index = ord(letter) - ord('a')
            if root.charList[index] == None:
                return False
            root = root.charList[index]
        return root.endOfWord

    def startsWith(self, prefix: str) -> bool:
        root = self
        for letter in prefix:
            index = ord(letter) - ord('a')
            if root.charList[index] == None:
                return False
            root = root.charList[index]
        return True
