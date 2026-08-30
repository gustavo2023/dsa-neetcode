class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        longest = 0
        nums_set = set(nums)

        for n in nums:
            if n - 1 not in nums:
                count = 0

                while n + count in nums_set:
                    count += 1

                longest = max(longest, count)
        
        return longest

