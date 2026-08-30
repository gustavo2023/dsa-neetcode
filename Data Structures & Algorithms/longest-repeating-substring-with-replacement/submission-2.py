class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length, l, maxf = 0, 0, 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])
            replacements = (r - l + 1) - maxf

            if replacements > k:
                count[s[l]] -= 1
                l += 1

            max_length = max(max_length, r - l + 1)

        return max_length