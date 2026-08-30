class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            char_count = [0] * 26

            for char in word:
                char_count[ord(char) - ord("a")] += 1

            key = tuple(char_count)

            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
        
        return list(anagrams.values())


        