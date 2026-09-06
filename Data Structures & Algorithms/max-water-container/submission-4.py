class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l, r = 0, len(heights) - 1

        while l < r:
            curr_height = min(heights[l], heights[r])
            curr_water = (r - l) * curr_height

            max_water = max(max_water, curr_water)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_water