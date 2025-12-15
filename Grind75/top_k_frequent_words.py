# Using Max heap of size n
# Find frequency of word and add to heap
# Use 2nd parameter the word itself to sort in lex order
# TC: O(N log N), SC: O(N)
def topKFrequent(self, words: List[str], k: int) -> List[str]:
    heap = []
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    for word in count:
        heappush(heap, [-count[word], word])
    res = []
    for _ in range(k):
        res.append(heappop(heap)[1])
    return res


# Using Min heap of size K
# But when popping from heap when size exceeds K and there is a match
# Higher lex word should be popped, so directly putting word as 2nd parameter fails
# So use operator overloading by creating a class object
# And overload less than operator as it is the one used by heap
# Reverse the comparison logic there
# Then finally Pop all elements from heap, since min heap, will be in increasing order
# So reverse it finally
# TC: O(N log K), SC: O(K)
class Word:
    def __init__(self, word):
        self.word = word
    def __lt__(self, other):
        return self.word > other.word

def topKFrequent(self, words: List[str], k: int) -> List[str]:
    heap = []
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    for word in count:
        heappush(heap, [count[word], Word(word)])
        if len(heap) > k:
            heappop(heap)
    
    res = []
    for _ in range(k):
        res.append(heappop(heap)[1].word)
    res.reverse()
    return res