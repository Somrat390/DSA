from collections import defaultdict
def anagram(strs):
    anagram_map = defaultdict(list)
    for char in strs:
        sorted_char = ''.join(sorted(char))
        anagram_map[sorted_char].append(char)
    return anagram_map.values()

print(anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
