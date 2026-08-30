class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l, r = 0, len(heights) - 1

        while l < r:
            min_height = min(heights[l], heights[r])
            current_container = (r - l) * min_height
            max_water = max(max_water, current_container)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_water