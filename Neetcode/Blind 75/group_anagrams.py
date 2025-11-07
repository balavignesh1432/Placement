def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # Using hashMap where key is sorted, value is all anagrams
    # TC = O(N KlogK), SC - O(NK), where K is length of each string
    hashMap = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        hashMap[key].append(s)
    return list(hashMap.values())

    # Using hashMap where key is count bucket [Only lowercase], value is all anagrams
    # TC = O(NK), SC - O(NK), where K is length of each string
    hashMap = defaultdict(list)
    for string in strs:
        count = [0] * 26
        for s in string:
            count[ord(s) - ord('a')] += 1
        key = tuple(count)
        hashMap[key].append(string)
    return list(res.values())