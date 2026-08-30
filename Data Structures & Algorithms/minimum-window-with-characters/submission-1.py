class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        count_t, window = {}, {}

        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        need, have, l = len(count_t), 0, 0
        res, res_len = [-1, -1], float("infinity")

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in count_t and window[s[r]] == count_t[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res = [l, r]
                    
                window[s[l]] -= 1

                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                
                l += 1

        if res_len == float("infinity"):
            return ""
        
        return s[res[0]:res[1] + 1]
