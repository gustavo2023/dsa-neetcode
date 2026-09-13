class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_list = []
        l, r = 0, 0
        queue = collections.deque()

        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()

            queue.append(r)

            if l > queue[0]:
                queue.popleft()

            if r + 1 >= k:
                max_list.append(nums[queue[0]])
                l += 1

            r += 1

        return max_list