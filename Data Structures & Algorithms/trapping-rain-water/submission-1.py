class Solution:
    def trap(self, height: List[int]) -> int:
        max_water = 0
        l = 0
        r = len(height) - 1
        left_max = height[l]
        right_max = height[r]

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                max_water += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                max_water += right_max - height[r]

        return max_water