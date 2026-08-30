class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window, l = len(s1), 0
        count, window_count = {}, {}

        for char in s1:
            count[char] = count.get(char, 0) + 1

        for r in range(len(s2)):
            window_count[s2[r]] = window_count.get(s2[r], 0) + 1
            window_size = r - l + 1

            if window_size > window:
                window_count[s2[l]] -= 1
                
                if window_count[s2[l]] == 0:
                    del window_count[s2[l]]

                l += 1

            if window_count == count:
                return True

        return False