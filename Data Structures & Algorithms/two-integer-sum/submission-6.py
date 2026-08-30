class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes_map = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in indexes_map:
                return [indexes_map[difference], i]
            indexes_map[nums[i]] = i