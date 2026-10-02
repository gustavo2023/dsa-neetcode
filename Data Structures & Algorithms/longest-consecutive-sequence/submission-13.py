class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest_sequence = 0
        nums_set = set(nums)

        for n in nums_set:
            if n - 1 not in nums_set:
                curr_sequence = 1

                while n + curr_sequence in nums_set:
                    curr_sequence += 1

                longest_sequence = max(longest_sequence, curr_sequence)

        return longest_sequence

        