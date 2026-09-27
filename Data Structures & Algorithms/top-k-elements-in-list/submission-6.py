class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        nums_count = {}

        for n in nums:
            nums_count[n] = 1 + nums_count.get(n, 0)

        for key, value in nums_count.items():
            buckets[value].append(key)

        most_frequent_elements = []

        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                most_frequent_elements.append(num)

                if len(most_frequent_elements) == k:
                    return most_frequent_elements

        return most_frequen_elements