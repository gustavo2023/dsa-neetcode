class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups_map = {}
        
        for s in strs:
            char_freq = [0] * 26

            for char in s:
                char_freq[ord(char) - ord("a")] += 1
            
            tup_key = tuple(char_freq)
            
            if tup_key in groups_map:
                groups_map[tup_key].append(s)
            else:
                groups_map[tup_key] = [s]

        return list(groups_map.values())