class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        substring, l, max_freq = 0, 0, 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_freq = max(max_freq, count[s[r]])

            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            substring = max(substring, r - l + 1)

        return substring