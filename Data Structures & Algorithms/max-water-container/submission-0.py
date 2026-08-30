class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_container = 0
        l = 0
        r = len(heights) - 1

        while l != r:
            min_height = min(heights[l], heights[r])
            curr_container = (r - l) * min_height

            max_container = max(max_container, curr_container)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_container