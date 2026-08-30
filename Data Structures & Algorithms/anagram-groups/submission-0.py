class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = {}

        for string in strs:
            char_count = [0] * 26

            for char in string:
                char_count[ord(char) - ord("a")] += 1

            key = tuple(char_count)

            if key in anagrams_map:
                anagrams_map[key].append(string)
            else:
                anagrams_map[key] = [string]

        return list(anagrams_map.values())


        