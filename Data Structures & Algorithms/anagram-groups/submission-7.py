class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = {}

        for s in strs:
            char_count = [0] * 26

            for c in s:
                char_count[ord(c) - ord("a")] += 1

            key = tuple(char_count)

            if key in group_anagrams:
                group_anagrams[key].append(s)
            else:
                group_anagrams[key] = [s]

        return list(group_anagrams.values())