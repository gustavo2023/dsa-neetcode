class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""

        t_count, window = {}, {}

        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)

        have, need = 0, len(t_count)
        l = 0
        min_substring = [-1, -1]
        substring_len = float("infinity")

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in t_count and window[s[r]] == t_count[s[r]]:
                have += 1

                while have == need:
                    if (r - l + 1) < substring_len:
                        substring_len = r - l + 1
                        min_substring = [l, r]
                    
                    window[s[l]] -= 1

                    if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                        have -= 1
                    
                    l += 1

        if substring_len == float("infinity"):
            return ""
        
        return s[min_substring[0]:min_substring[1] + 1]
        