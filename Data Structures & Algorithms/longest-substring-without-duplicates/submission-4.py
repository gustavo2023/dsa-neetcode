class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l = 0
        chars_set = set()
        longest_substring = 0

        for r in range(len(s)):
            while s[r] in chars_set:
                chars_set.discard(s[l])
                l += 1

            chars_set.add(s[r])
            longest_substring = max(longest_substring, r - l + 1)

        return longest_substring