class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = {}

        for s in strs:
            chars_count = [0] * 26

            for c in s:
                chars_count[ord(c) - ord("a")] += 1

            key = tuple(chars_count)
            if key in anagrams_map:
                anagrams_map[key].append(s)
            else:
                anagrams_map[key] = [s]

        return list(anagrams_map.values())