class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window, l = len(s1), 0
        count = [0] * 26
        window_count = [0] * 26

        for char in s1:
            count[ord(char) - ord("a")] += 1

        for r in range(len(s2)):
            window_count[ord(s2[r]) - ord("a")] += 1
            window_size = r - l + 1

            if window_size > window:
                index = ord(s2[l]) - ord("a")
                window_count[index] -= 1
                l += 1

            if window_count == count:
                return True

        return False

