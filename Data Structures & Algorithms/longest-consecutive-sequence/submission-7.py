class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest = 0

        for num in nums:
            if num - 1 not in nums:
                count = 0

                while num + count in nums:
                    count += 1

                longest = max(longest, count)

        return longest


