class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums_set = set(nums)
        longest = 0

        for n in nums_set:
            if n - 1 not in nums_set:
                curr_length = 0

                while n + curr_length in nums_set:
                    curr_length += 1

                longest = max(longest, curr_length)

        return longest

