class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
                
            l, r = i + 1, len(nums) - 1

            while l < r:
                val = nums[i] + nums[l] + nums[r]

                if val > 0:
                    r -= 1
                elif val < 0:
                    l += 1
                else:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l - 1] == nums[l]:
                        l += 1

        return triplets