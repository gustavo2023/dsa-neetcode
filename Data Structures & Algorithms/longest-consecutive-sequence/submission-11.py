class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums_set = set(nums)
        max_sequence = 0

        for n in nums:
            if n - 1 not in nums_set:
                count = 0

                while n + count in nums_set:
                    count += 1

                max_sequence = max(max_sequence, count)

        return max_sequence
        