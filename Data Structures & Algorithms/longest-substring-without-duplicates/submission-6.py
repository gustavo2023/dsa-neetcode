class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l = 0
        chars_set = set()
        substring = 0

        for r in range(len(s)):
            while s[r] in chars_set:
                chars_set.discard(s[l])
                l += 1

            chars_set.add(s[r])
            substring = max(substring, r - l + 1)

        return substring